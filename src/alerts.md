# Real-Time Alert System for Suspicious Transactions

This module integrates AI models to detect flagged transactions and generate real-time alerts. Below are the implemented functionalities and API endpoints:

## 1. Features
- Detect flagged transactions based on risk patterns.
- Generate real-time alerts.
- Display transaction details, risk indicators, and actions on the dashboard.
- Allow escalation for critical transactions.

## 2. API Endpoints
### POST /alerts/new
- **Description:** Generates a new alert for a flagged transaction.
- **Request Body:**
```json
{
  "transactionId": "string",
  "amount": "number",
  "customerDetails": {
    "name": "string",
    "accountId": "string"
  },
  "riskScore": "number",
  "historicalFlags": "boolean"
}
```
- **Response:**
```json
{
  "alertId": "string",
  "transactionId": "string",
  "riskIndicators": ["string"],
  "timestamp": "string"
}
```

### GET /alerts/details/{alertId}
- **Description:** Retrieves details for a specific alert.
- **Response:**
```json
{
  "alertId": "string",
  "transactionId": "string",
  "riskIndicators": ["string"],
  "timestamp": "string",
  "escalationStatus": "boolean"
}
```

### PATCH /alerts/escalate/{alertId}
- **Description:** Marks a flagged alert as escalated.
- **Response:**
```json
{
  "alertId": "string",
  "transactionId": "string",
  "escalationStatus": true
}
```

## 3. JSON Schema
### Transaction
```json
{
  "transactionId": "string",
  "amount": "number",
  "customerDetails": {
    "name": "string",
    "accountId": "string"
  },
  "riskScore": "number",
  "historicalFlags": "boolean"
}
```

### Alert
```json
{
  "alertId": "string",
  "transactionId": "string",
  "riskIndicators": ["string"],
  "timestamp": "string",
  "escalationStatus": "boolean"
}
```

## 4. Testability
- Check instant alert generation upon detecting flagged transactions.
- Verify transaction details appear correctly on the dashboard.
- Simulate escalation for critical transactions.

## Dependencies
- Active AI models for risk detection.
- Compliance system integrations for flagged transaction reporting.