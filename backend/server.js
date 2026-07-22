const express = require('express');
const WebSocket = require('ws');
const app = express();
const port = 3000;

// Example metrics
const metrics = {
  inventoryAccuracy: 95,
  orderProcessingTime: 22,
  leadTime: 11
};

app.use(express.json());

app.get('/metrics', (req, res) => {
  res.json(metrics);
});

app.post('/alert-config', (req, res) => {
  // Logic to handle KPI thresholds
  res.status(201).send('Alert configuration saved.');
});

const wss = new WebSocket.Server({ noServer: true });
wss.on('connection', (ws) => {
  ws.send(JSON.stringify({ type: 'real-time-update', data: metrics }));
});

app.listen(port, () => {
  console.log(`Backend server running at http://localhost:${port}`);
});