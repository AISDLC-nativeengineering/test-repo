import React, { useEffect } from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, expect, it, vi } from 'vitest';
import {
  MODULES,
  fetchModules,
  UnsavedChangesProvider,
  useUnsavedChanges,
  UnsavedChangesModal,
} from './FinancialDashboardNavigation';

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
});
