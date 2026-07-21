import React, { useState, useEffect } from 'react';

const Dashboard = () => {
    const [status, setStatus] = useState('Inactive');
    const [route, setRoute] = useState({ latitude: null, longitude: null });
    const [metrics, setMetrics] = useState([]);

    useEffect(() => {
        // Fetch driving status and route
        fetch('/dashboard/status')
            .then(response => response.json())
            .then(data => {
                setStatus(data.status);
                setRoute(data.route);
            })
            .catch(err => console.error('Error fetching status:', err));

        // Fetch safety metrics every 10 seconds
        const metricsInterval = setInterval(() => {
            fetch('/dashboard/metrics')
                .then(response => response.json())
                .then(data => setMetrics(data.metrics))
                .catch(err => console.error('Error fetching metrics:', err));
        }, 10000);

        return () => clearInterval(metricsInterval);
    }, []);

    return (
        <div className="dashboard">
            <h1>Driving System Dashboard</h1>
            <div className="status">
                <p><strong>Status:</strong> {status}</p>
            </div>
            <div className="map">
                <h2>Live Route</h2>
                {route.latitude && route.longitude ? (
                    <p>Location: {route.latitude}, {route.longitude}</p>
                ) : (
                    <p>Loading route data...</p>
                )}
            </div>
            <div className="metrics">
                <h2>Safety Metrics</h2>
                <ul>
                    {metrics.map((metric, index) => (
                        <li key={index}>{metric.type}: {metric.value}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default Dashboard;