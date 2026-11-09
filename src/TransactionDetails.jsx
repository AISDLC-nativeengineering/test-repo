import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './TransactionDetails.css';

const TransactionDetails = ({ transactionId, goBack }) => {
    const [transactionDetails, setTransactionDetails] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchTransactionDetails = async () => {
            try {
                const response = await axios.get(`/api/transactions/${transactionId}/details`);
                setTransactionDetails(response.data);
            } catch (err) {
                setError('Failed to fetch transaction details!');
            }
        };

        if (transactionId) {
            fetchTransactionDetails();
        }
    }, [transactionId]);

    if (error) {
        return <div className="error">{error}</div>;
    }

    if (!transactionDetails) {
        return <div>Loading transaction details...</div>;
    }

    return (
        <div className="transaction-details">
            <h1>Transaction Details</h1>
            <div className="transaction-metadata">
                <p><strong>ID:</strong> {transactionDetails.id}</p>
                <p><strong>Amount:</strong> {transactionDetails.amount}</p>
                <p><strong>Timestamp:</strong> {transactionDetails.timestamp}</p>
                <p><strong>Type:</strong> {transactionDetails.type}</p>
            </div>
            <div className="ml-risk-score">
                <h2>ML Risk Score</h2>
                <p>{transactionDetails.mlRiskScore}</p>
            </div>
            <div className="fraud-detection">
                <h2>Matched Fraud Rules</h2>
                <ul>
                    {transactionDetails.matchedFraudRules.map((rule, index) => (
                        <li key={index}>{rule}</li>
                    ))}
                </ul>
            </div>
            <button onClick={goBack} className="back-button">Back to Dashboard</button>
        </div>
    );
};

export default TransactionDetails;