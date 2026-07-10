import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './DashboardInsights.css';

const DashboardInsights = () => {
    const [metrics, setMetrics] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchMetrics = async () => {
            try {
                const response = await axios.get('/api/dashboard/insights', {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('authToken')}`,
                    },
                });
                setMetrics(response.data);
            } catch (err) {
                setError('Failed to load dashboard metrics');
            }
        };

        fetchMetrics();
    }, []);

    if (error) {
        return <div className="error">{error}</div>;
    }

    if (!metrics) {
        return <div className="loading">Loading...</div>;
    }

    return (
        <div className="dashboard-insights">
            <h1>Cybersecurity Dashboard</h1>
            <div className="metrics">
                <div className="metric">
                    <p>Active Threats</p>
                    <h2>{metrics.activeThreats}</h2>
                </div>
                <div className="metric">
                    <p>Incident Resolutions</p>
                    <h2>{metrics.incidentResolutions}</h2>
                </div>
                <div className="metric">
                    <p>Compliance Percentage</p>
                    <h2>{metrics.compliancePercentage}%</h2>
                </div>
            </div>
            <div className="actions">
                <button onClick={() => window.location.href = '/threat-details'}>View Threats</button>
                <button onClick={() => window.location.href = '/incident-management'}>Manage Incidents</button>
                <button onClick={() => window.location.href = '/compliance-reports'}>Compliance Reports</button>
            </div>
        </div>
    );
};

export default DashboardInsights;