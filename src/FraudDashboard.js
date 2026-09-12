import React, { useState, useEffect } from 'react';
import { fetchAlerts, fetchKPIs } from './api';
import Filters from './Filters';
import KPIs from './KPIs';

const FraudDashboard = () => {
  const [alerts, setAlerts] = useState([]);
  const [kpis, setKpis] = useState([]);

  useEffect(() => {
    const getAlerts = async () => {
      const data = await fetchAlerts();
      setAlerts(data);
    };

    const getKPIs = async () => {
      const data = await fetchKPIs();
      setKpis(data);
    };

    getAlerts();
    getKPIs();
  }, []);

  const handleFilter = async (filters) => {
    const filteredAlerts = await fetchAlerts(filters);
    setAlerts(filteredAlerts);
  };

  return (
    <div>
      <h1>Fraud Alerts Dashboard</h1>
      <Filters onFilter={handleFilter} />
      <KPIs data={kpis} />
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Type</th>
            <th>Risk Score</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((alert) => (
            <tr key={alert.ID}>
              <td>{alert.ID}</td>
              <td>{alert.type}</td>
              <td>{alert.riskScore}</td>
              <td>{alert.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default FraudDashboard;