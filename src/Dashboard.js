import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [alerts, setAlerts] = useState([]);
  const [report, setReport] = useState(null);

  useEffect(() => {
    // Fetch alerts
    axios.get('/dashboard/alerts')
      .then(response => setAlerts(response.data))
      .catch(error => console.error('Error fetching alerts:', error));
  }, []);

  const requestReport = () => {
    axios.get('/dashboard/report?type=lifecycle')
      .then(response => setReport(response.data.content))
      .catch(error => console.error('Error generating report:', error));
  };

  return (
    <div>
      <h1>Maintenance Dashboard</h1>

      {/* Alerts */}
      <section>
        <h2>Alerts</h2>
        <ul>
          {alerts.map(alert => (
            <li key={alert.id}>{alert.details} - {new Date(alert.timestamp).toLocaleString()}</li>
          ))}
        </ul>
      </section>

      {/* Report Generation */}
      <section>
        <h2>Generate Lifecycle Report</h2>
        <button onClick={requestReport}>Generate Report</button>
        {report && (
          <div>
            <h3>Report:</h3>
            <p>{report}</p>
          </div>
        )}
      </section>
    </div>
  );
};

export default Dashboard;