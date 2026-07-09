// Frontend implementation for analytics dashboard
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Dashboard = () => {
    const [metrics, setMetrics] = useState([]);
    const [recommendations, setRecommendations] = useState([]);
    const [filter, setFilter] = useState({ startDate: '', endDate: '' });
    const [noData, setNoData] = useState(false);

    useEffect(() => {
        if (filter.startDate && filter.endDate) {
            axios.get('/analytics/wellness', { params: filter })
                .then(response => {
                    setMetrics(response.data.metrics);
                    setRecommendations(response.data.recommendations);
                    setNoData(response.data.metrics.length === 0);
                })
                .catch(err => console.error('Error fetching analytics data:', err));
        }
    }, [filter]);

    const handleExport = () => {
        axios.post('/analytics/export', filter, { responseType: 'blob' })
            .then(response => {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'analytics.csv');
                document.body.appendChild(link);
                link.click();
            })
            .catch(err => console.error('Error exporting analytics data:', err));
    };

    return (
        <div>
            <h1>HR Analytics Dashboard</h1>
            <div>
                <label>Start Date:</label>
                <input type="date" onChange={(e) => setFilter({ ...filter, startDate: e.target.value })} />
                <label>End Date:</label>
                <input type="date" onChange={(e) => setFilter({ ...filter, endDate: e.target.value })} />
            </div>
            {noData ? (
                <div>No data available</div>
            ) : (
                <div>
                    <h2>Metrics</h2>
                    {metrics.map((metric, index) => (
                        <p key={index}>{metric.category}: {metric.value}%</p>
                    ))}
                    <h2>Recommendations</h2>
                    {recommendations.map((rec, index) => (
                        <p key={index}>{rec.priority}: {rec.text}</p>
                    ))}
                </div>
            )}
            <button onClick={handleExport}>Export CSV</button>
        </div>
    );
};

export default Dashboard;