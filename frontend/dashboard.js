import React, { useEffect, useState } from 'react';
import { Chart } from 'react-chartjs-2';

function Dashboard() {
  const [metrics, setMetrics] = useState({});
  const [alerts, setAlerts] = useState([]);

  // Fetch metrics on load
  useEffect(() => {
    const fetchMetrics = async () => {
      const response = await fetch('/metrics');
      const data = await response.json();
      setMetrics(data);
    };
    fetchMetrics();

    // Listen for real-time updates
    const ws = new WebSocket('ws://localhost:3000');
    ws.onmessage = (msg) => {
      const message = JSON.parse(msg.data);
      if (message.type === 'real-time-update') {
        setMetrics(message.data);
      }
    };

    return () => ws.close();
  }, []);

  const chartData = {
    labels: ['Inventory Accuracy', 'Order Processing Time', 'Lead Time'],
    datasets: [
      {
        label: 'Metrics',
        data: [metrics.inventoryAccuracy, metrics.orderProcessingTime, metrics.leadTime],
        backgroundColor: ['rgba(75,192,192,0.4)'],
      },
    ],
  };

  return (
    <div>
      <h1>Supply Chain Dashboard</h1>
      <Chart type="bar" data={chartData} />
      <div>
        {alerts.map((alert, index) => (
          <p key={index} style={{ color: 'red' }}>
            {alert.description} - {alert.timestamp}
          </p>
        ))}
      </div>
    </div>
  );
}

export default Dashboard;