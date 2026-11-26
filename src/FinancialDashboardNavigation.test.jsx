import React, { useEffect } from 'react';
import { cleanup, render, screen } from '@testing-library/react';
import { RouterProvider } from 'react-router-dom';
import userEvent from '@testing-library/user-event';
import { afterEach, describe, expect, it, vi } from 'vitest';
import {
  MODULES,
  createFinancialDashboardRouter,
  fetchModules,
  UnsavedChangesProvider,
  useUnsavedChanges,
  UnsavedChangesModal,
} from './FinancialDashboardNavigation';

afterEach(() => {
  cleanup();
  window.history.replaceState({}, '', '/');
});

describe('dashboard module navigation', () => {
  it('loads the four supported modules from the modules API', async () => {
    const response = {
      ok: true,
      json: vi.fn().mockResolvedValue({ modules: MODULES }),
    };
    await expect(fetchModules(vi.fn().mockResolvedValue(response))).resolves.toEqual(MODULES);
  });

  it('falls back to the supported modules for an invalid API payload', async () => {
    const response = { ok: true, json: vi.fn().mockResolvedValue({ modules: [] }) };
    await expect(fetchModules(vi.fn().mockResolvedValue(response))).resolves.toEqual(MODULES);
  });

  it('allows users to cancel navigation at the unsaved changes prompt', async () => {
    const blocker = { state: 'blocked', proceed: vi.fn(), reset: vi.fn() };
    render(<UnsavedChangesModal blocker={blocker} activeModule="Transactions" />);
    await userEvent.click(screen.getByRole('button', { name: 'Cancel' }));
    expect(blocker.reset).toHaveBeenCalledOnce();
  });

  it('provides unsaved and save-handler state to module screens', () => {
    const TestScreen = () => {
      const unsaved = useUnsavedChanges('transactions');
      useEffect(() => {
        unsaved.setUnsaved(true);
        unsaved.registerSaveHandler(vi.fn());
      }, []);
      return <div>Test screen</div>;
    };
    render(<UnsavedChangesProvider><TestScreen /></UnsavedChangesProvider>);
    expect(screen.getByText('Test screen')).toBeInTheDocument();
  });

  it('renders the category editor in the Transactions module', async () => {
    window.history.replaceState({}, '', '/modules/transactions');
    const router = createFinancialDashboardRouter();

    render(
      <UnsavedChangesProvider>
        <RouterProvider router={router} />
      </UnsavedChangesProvider>,
    );

    expect(
      await screen.findByRole('heading', { name: 'Transactions' }),
    ).toBeInTheDocument();
    expect(screen.getByText('Green Grocer')).toBeInTheDocument();
  });
});
