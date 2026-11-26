import React, { useState } from 'react';

import './TransactionCategoryEditor.css';

export const CATEGORIES = [
  'Dining',
  'Food',
  'Groceries',
  'Shopping',
  'Transport',
  'Travel',
  'Utilities',
];

export const MOCK_TRANSACTIONS = [
  {
    id: 'txn-1001',
    merchant: 'Green Grocer',
    currentCategory: 'Shopping',
    suggestedCategories: ['Groceries', 'Food'],
  },
  {
    id: 'txn-1002',
    merchant: 'Metro Transit',
    currentCategory: 'Transport',
    suggestedCategories: ['Travel', 'Utilities'],
  },
  {
    id: 'txn-1003',
    merchant: 'Corner Cafe',
    currentCategory: 'Dining',
    suggestedCategories: ['Food', 'Groceries'],
  },
];

const cloneTransactions = (transactions) =>
  transactions.map((transaction) => ({
    ...transaction,
    suggestedCategories: [...transaction.suggestedCategories],
  }));

const TransactionCategoryEditor = () => {
  const [transactions, setTransactions] = useState(() =>
    cloneTransactions(MOCK_TRANSACTIONS),
  );
  const [drafts, setDrafts] = useState({});
  const [selectedIds, setSelectedIds] = useState(() => new Set());
  const [bulkCategory, setBulkCategory] = useState('');
  const [statusMessage, setStatusMessage] = useState('');

  const updateDraft = (transaction, category = transaction.currentCategory) => {
    setDrafts((current) => ({ ...current, [transaction.id]: category }));
    setStatusMessage('');
  };

  const cancelEdit = (transaction) => {
    setDrafts((current) => {
      const next = { ...current };
      delete next[transaction.id];
      return next;
    });
    setStatusMessage(`Changes canceled for ${transaction.merchant}.`);
  };

  const saveEdit = (transaction) => {
    const category = drafts[transaction.id];
    if (!CATEGORIES.includes(category)) return;

    setTransactions((current) =>
      current.map((item) =>
        item.id === transaction.id ? { ...item, currentCategory: category } : item,
      ),
    );
    setDrafts((current) => {
      const next = { ...current };
      delete next[transaction.id];
      return next;
    });
    setStatusMessage(`Category saved for ${transaction.merchant}.`);
  };

  const toggleSelection = (transactionId) => {
    setSelectedIds((current) => {
      const next = new Set(current);
      if (next.has(transactionId)) next.delete(transactionId);
      else next.add(transactionId);
      return next;
    });
    setStatusMessage('');
  };

  const applyBulkCategory = () => {
    if (!bulkCategory || selectedIds.size === 0) return;

    const updatedCount = selectedIds.size;
    setTransactions((current) =>
      current.map((transaction) =>
        selectedIds.has(transaction.id)
          ? { ...transaction, currentCategory: bulkCategory }
          : transaction,
      ),
    );
    setDrafts((current) =>
      Object.fromEntries(
        Object.entries(current).filter(([transactionId]) =>
          !selectedIds.has(transactionId),
        ),
      ),
    );
    setSelectedIds(new Set());
    setBulkCategory('');
    setStatusMessage(
      `Updated ${updatedCount} transactions to ${bulkCategory}.`,
    );
  };

  return (
    <section className="transaction-categories" aria-labelledby="transactions-heading">
      <h1 id="transactions-heading">Transactions</h1>
      <p>Review and update transaction categories using the suggested matches.</p>

      <div className="transaction-bulk-actions">
        <label htmlFor="bulk-category">Category for selected transactions</label>
        <select
          id="bulk-category"
          value={bulkCategory}
          onChange={(event) => setBulkCategory(event.target.value)}
        >
          <option value="">Choose a category</option>
          {CATEGORIES.map((category) => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
        <button
          type="button"
          onClick={applyBulkCategory}
          disabled={!bulkCategory || selectedIds.size === 0}
        >
          Update selected
        </button>
        <span aria-live="polite">
          {selectedIds.size} selected
        </span>
      </div>

      <table className="transaction-table">
        <thead>
          <tr>
            <th scope="col">Select</th>
            <th scope="col">Transaction</th>
            <th scope="col">Category</th>
            <th scope="col">Category editor</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((transaction) => {
            const isEditing = Object.hasOwn(drafts, transaction.id);
            return (
              <tr key={transaction.id}>
                <td>
                  <input
                    type="checkbox"
                    aria-label={`Select transaction ${transaction.id}`}
                    checked={selectedIds.has(transaction.id)}
                    onChange={() => toggleSelection(transaction.id)}
                  />
                </td>
                <td>
                  <span>{transaction.merchant}</span>
                  <small>{transaction.id}</small>
                </td>
                <td>{transaction.currentCategory}</td>
                <td>
                  {isEditing ? (
                    <div className="category-editor">
                      <label htmlFor={`category-${transaction.id}`}>
                        Choose category for {transaction.id}
                      </label>
                      <select
                        id={`category-${transaction.id}`}
                        value={drafts[transaction.id]}
                        onChange={(event) =>
                          updateDraft(transaction, event.target.value)
                        }
                      >
                        {CATEGORIES.map((category) => (
                          <option key={category} value={category}>
                            {category}
                          </option>
                        ))}
                      </select>
                      <div className="category-suggestions">
                        <span>Suggestions:</span>
                        {transaction.suggestedCategories.map((category) => (
                          <button
                            key={category}
                            type="button"
                            onClick={() => updateDraft(transaction, category)}
                          >
                            {category}
                          </button>
                        ))}
                      </div>
                      <div className="category-editor-actions">
                        <button
                          type="button"
                          onClick={() => saveEdit(transaction)}
                        >
                          Save category
                        </button>
                        <button
                          type="button"
                          onClick={() => cancelEdit(transaction)}
                        >
                          Cancel edit
                        </button>
                      </div>
                    </div>
                  ) : (
                    <button
                      type="button"
                      onClick={() => updateDraft(transaction)}
                    >
                      Edit category
                    </button>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <p className="category-status" role="status">
        {statusMessage}
      </p>
    </section>
  );
};

export default TransactionCategoryEditor;
