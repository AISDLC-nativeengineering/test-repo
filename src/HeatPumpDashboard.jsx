import React, { useState, useEffect } from 'react';
import Chart from 'chart.js/auto';

const HeatPumpDashboard = () => {
  const [data, setData] = useState([]);
  const [filter, setFilter] = useState('All');
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('/heatpumps/status');
        if (response.status === 503) {
          setError('Unable to load status, retry later');
          return;
        }
        const result = await response.json();
        setData(result.data);
      } catch (err) {
        setError('An unexpected error occurred');
      }
    };

    fetchData();
  }, []);

  const filteredData = data.filter((item) => filter === 'All' || item.status === filter);

  return (
    <div className="dashboard">
      <h1>Heat Pump Dashboard</h1>

      {error && <div className="error-message">{error}</div>}

      {data.length === 0 && !error && (
        <div className="empty-state">No devices connected yet. Please set up your IoT sensors.</div>
      )}

      {!error && data.length > 0 && (
        <>
          <div className="filter-buttons">
            <button onClick={() => setFilter('All')}>All</button>
            <button onClick={() => setFilter('Critical')}>Critical</button>
          </div>

          <div className="statuses">
            {filteredData.map((device) => (
              <div key={device.deviceId} className={`status-tile ${device.status.toLowerCase()}`}>
                <h2>{device.deviceId}</h2>
                <p>Status: {device.status}</p>
                <p>Last Updated: {new Date(device.lastUpdated).toLocaleString()}</p>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
};

export default HeatPumpDashboard;