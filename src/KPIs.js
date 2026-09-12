import React from 'react';

const KPIs = ({ data }) => {
  return (
    <div>
      <h2>Fraud KPIs</h2>
      <table>
        <thead>
          <tr>
            <th>Metric</th>
            <th>Value</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {data.map((kpi, index) => (
            <tr key={index}>
              <td>{kpi.metricName}</td>
              <td>{kpi.value}</td>
              <td>{new Date(kpi.timestamp).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default KPIs;