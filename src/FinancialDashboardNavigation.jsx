import React, { useContext, useEffect, useMemo, useState } from 'react';
import {
  NavLink,
  Outlet,
  Route,
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
  useBlocker,
  useLocation,
} from 'react-router-dom';
import './FinancialDashboardNavigation.css';

export const MODULES = [
  { key: 'overview', title: 'Overview' },
  { key: 'transactions', title: 'Transactions' },
  { key: 'reports', title: 'Reports' },
  { key: 'data_sources', title: 'Data Sources' },
];

const UnsavedChangesContext = React.createContext({
  setUnsaved: () => {},
  registerSaveHandler: () => () => {},
  clearSaveHandler: () => {},
  hasUnsavedChanges: false,
  getSaveHandler: () => undefined,
});

export const UnsavedChangesProvider = ({ children }) => {
  const [unsavedModules, setUnsavedModules] = useState(new Map());
  const [saveHandlers, setSaveHandlers] = useState(new Map());

  const setUnsaved = (module, hasUnsavedChanges) => {
    setUnsavedModules((current) => {
      const next = new Map(current);
      if (hasUnsavedChanges) next.set(module, true);
      else next.delete(module);
      return next;
    });
  };

  const registerSaveHandler = (module, handler) => {
    setSaveHandlers((current) => new Map(current).set(module, handler));
    return () => setSaveHandlers((current) => {
      const next = new Map(current);
      next.delete(module);
      return next;
    });
  };

  const clearSaveHandler = (module) => {
    setSaveHandlers((current) => {
      const next = new Map(current);
      next.delete(module);
      return next;
    });
  };

  const value = useMemo(() => ({
    setUnsaved,
    registerSaveHandler,
    clearSaveHandler,
    hasUnsavedChanges: unsavedModules.size > 0,
    getSaveHandler: (module) => saveHandlers.get(module),
  }), [unsavedModules, saveHandlers]);

  useEffect(() => {
    const handleBeforeUnload = (event) => {
      if (unsavedModules.size === 0) return;
      event.preventDefault();
      event.returnValue = '';
    };
    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, [unsavedModules]);

  return (
    <UnsavedChangesContext.Provider value={value}>
      {children}
    </UnsavedChangesContext.Provider>
  );
};

export const useUnsavedChanges = (module) => {
  const context = useContext(UnsavedChangesContext);
  return {
    setUnsaved: (value) => context.setUnsaved(module, value),
    registerSaveHandler: (handler) => context.registerSaveHandler(module, handler),
  };
};

export const fetchModules = async (fetchImpl = fetch) => {
  const response = await fetchImpl('/api/modules/info');
  if (!response.ok) throw new Error('Failed to fetch modules info.');
  const payload = await response.json();
  if (!payload || !Array.isArray(payload.modules)) {
    throw new Error('Invalid modules response.');
  }
  const configuredKeys = new Set(MODULES.map((module) => module.key));
  const modules = payload.modules.filter((module) =>
    module && typeof module.key === 'string' &&
    configuredKeys.has(module.key) && typeof module.title === 'string'
  );
  return modules.length === MODULES.length ? modules : MODULES;
};

export const UnsavedChangesModal = ({ blocker, activeModule }) => {
  if (blocker.state !== 'blocked') return null;

  const handleSave = async () => {
    if (blocker.saveHandler) await blocker.saveHandler();
    if (blocker.clearUnsaved) blocker.clearUnsaved();
    blocker.proceed();
  };

  const handleProceed = () => {
    if (blocker.clearUnsaved) blocker.clearUnsaved();
    blocker.proceed();
  };

  return (
    <div className="unsaved-modal-backdrop" role="presentation">
      <div className="unsaved-modal" role="dialog" aria-modal="true" aria-labelledby="unsaved-modal-title">
        <h2 id="unsaved-modal-title">Unsaved changes</h2>
        <p>You have unsaved changes in {activeModule}. Save or proceed?</p>
        <div className="unsaved-modal-actions">
          <button type="button" onClick={blocker.reset}>Cancel</button>
          <button type="button" onClick={handleSave}>Save</button>
          <button type="button" onClick={handleProceed}>Proceed</button>
        </div>
      </div>
    </div>
  );
};

const ModuleLayout = ({ modules }) => {
  const location = useLocation();
  const unsavedContext = useContext(UnsavedChangesContext);
  const activeKey = location.pathname.split('/').filter(Boolean)[0] || 'overview';
  const activeModule = MODULES.find((module) => module.key === activeKey)?.title || 'this module';
  const blocker = useBlocker(({ currentLocation, nextLocation }) =>
    unsavedContext.hasUnsavedChanges &&
    currentLocation.pathname !== nextLocation.pathname
  );
  const enrichedBlocker = blocker.state === 'blocked' ? {
    ...blocker,
    saveHandler: unsavedContext.getSaveHandler(activeKey),
    clearUnsaved: () => unsavedContext.setUnsaved(activeKey, false),
  } : blocker;

  return (
    <div className="financial-dashboard">
      <a className="skip-link" href="#dashboard-content">Skip to main content</a>
      <aside className="dashboard-sidebar" aria-label="Dashboard modules">
        <nav className="dashboard-navigation">
          {modules.map((module) => (
            <NavLink
              key={module.key}
              to={`/modules/${module.key}`}
              className={({ isActive }) => isActive ? 'module-link module-link-active' : 'module-link'}
            >
              {module.title}
            </NavLink>
          ))}
        </nav>
      </aside>
      <main id="dashboard-content" className="dashboard-content"><Outlet /></main>
      {blocker.state === 'blocked' && (
        <UnsavedChangesModal blocker={enrichedBlocker} activeModule={activeModule} />
      )}
    </div>
  );
};

export const ModulePlaceholder = ({ moduleKey, title }) => (
  <section aria-labelledby={`${moduleKey}-heading`}>
    <h1 id={`${moduleKey}-heading`}>{title}</h1>
  </section>
);

export const createFinancialDashboardRouter = (modules = MODULES) =>
  createBrowserRouter(createRoutesFromElements(
    <Route path="/" element={<ModuleLayout modules={modules} />}>
      <Route index element={<ModulePlaceholder moduleKey="overview" title="Overview" />} />
      {modules.map((module) => (
        <Route
          key={module.key}
          path={`modules/${module.key}`}
          element={<ModulePlaceholder moduleKey={module.key} title={module.title} />}
        />
      ))}
    </Route>
  ));

const FinancialDashboardNavigation = () => {
  const [modules, setModules] = useState(MODULES);

  useEffect(() => {
    let cancelled = false;
    fetchModules()
      .then((loadedModules) => { if (!cancelled) setModules(loadedModules); })
      .catch(() => { if (!cancelled) setModules(MODULES); });
    return () => { cancelled = true; };
  }, []);

  const router = useMemo(() => createFinancialDashboardRouter(modules), [modules]);
  return (
    <UnsavedChangesProvider>
      <RouterProvider router={router} />
    </UnsavedChangesProvider>
  );
};

export default FinancialDashboardNavigation;
