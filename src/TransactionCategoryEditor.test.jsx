import React from 'react';
import { cleanup, render, screen, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { afterEach, describe, expect, it } from 'vitest';

import TransactionCategoryEditor from './TransactionCategoryEditor';

afterEach(cleanup);

const getTransactionRow = (id) => {
  const transactionId = screen.getByText(id);
  return transactionId.closest('tr');
};

describe('transaction category editor', () => {
  it('shows suggestions and saves a changed category', async () => {
    const user = userEvent.setup();
    render(<TransactionCategoryEditor />);

    const row = getTransactionRow('txn-1001');
    await user.click(within(row).getByRole('button', { name: 'Edit category' }));
    expect(within(row).getByText('Suggestions:')).toBeInTheDocument();

    await user.click(within(row).getByRole('button', { name: 'Groceries' }));
    await user.click(
      within(row).getByRole('button', { name: 'Save category' }),
    );

    expect(within(row).getByText('Groceries')).toBeInTheDocument();
    expect(screen.getByRole('status')).toHaveTextContent(
      'Category saved for Green Grocer.',
    );
  });

  it('discards a draft when the user cancels editing', async () => {
    const user = userEvent.setup();
    render(<TransactionCategoryEditor />);

    const row = getTransactionRow('txn-1001');
    await user.click(within(row).getByRole('button', { name: 'Edit category' }));
    await user.selectOptions(
      within(row).getByLabelText('Choose category for txn-1001'),
      'Food',
    );
    await user.click(within(row).getByRole('button', { name: 'Cancel edit' }));

    expect(within(row).getByText('Shopping')).toBeInTheDocument();
    expect(within(row).queryByText('Food')).not.toBeInTheDocument();
    expect(screen.getByRole('status')).toHaveTextContent(
      'Changes canceled for Green Grocer.',
    );
  });

  it('updates all selected transactions to the chosen bulk category', async () => {
    const user = userEvent.setup();
    render(<TransactionCategoryEditor />);

    await user.click(
      screen.getByRole('checkbox', { name: 'Select transaction txn-1001' }),
    );
    await user.click(
      screen.getByRole('checkbox', { name: 'Select transaction txn-1002' }),
    );
    await user.selectOptions(
      screen.getByLabelText('Category for selected transactions'),
      'Travel',
    );
    await user.click(screen.getByRole('button', { name: 'Update selected' }));

    expect(within(getTransactionRow('txn-1001')).getByText('Travel')).toBeInTheDocument();
    expect(within(getTransactionRow('txn-1002')).getByText('Travel')).toBeInTheDocument();
    expect(within(getTransactionRow('txn-1003')).getByText('Dining')).toBeInTheDocument();
    expect(screen.getByRole('status')).toHaveTextContent(
      'Updated 2 transactions to Travel.',
    );
    expect(
      screen.getByRole('checkbox', { name: 'Select transaction txn-1001' }),
    ).not.toBeChecked();
  });

  it('keeps bulk update disabled until a category and selection are present', async () => {
    const user = userEvent.setup();
    render(<TransactionCategoryEditor />);
    const updateButton = screen.getByRole('button', { name: 'Update selected' });

    expect(updateButton).toBeDisabled();
    await user.click(
      screen.getByRole('checkbox', { name: 'Select transaction txn-1001' }),
    );
    expect(updateButton).toBeDisabled();
    await user.selectOptions(
      screen.getByLabelText('Category for selected transactions'),
      'Food',
    );
    expect(updateButton).toBeEnabled();
  });

  it('closes an open draft when that transaction is updated in bulk', async () => {
    const user = userEvent.setup();
    render(<TransactionCategoryEditor />);

    await user.click(
      screen.getByRole('checkbox', { name: 'Select transaction txn-1001' }),
    );
    const row = getTransactionRow('txn-1001');
    await user.click(within(row).getByRole('button', { name: 'Edit category' }));
    await user.selectOptions(
      within(row).getByLabelText('Choose category for txn-1001'),
      'Food',
    );
    await user.selectOptions(
      screen.getByLabelText('Category for selected transactions'),
      'Travel',
    );
    await user.click(screen.getByRole('button', { name: 'Update selected' }));

    expect(within(row).getByText('Travel')).toBeInTheDocument();
    expect(
      within(row).getByRole('button', { name: 'Edit category' }),
    ).toBeInTheDocument();
  });
});
