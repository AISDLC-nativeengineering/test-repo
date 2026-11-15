import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FinancialDashboard = () => {
  const [widgets, setWidgets] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch widgets data on component mount
    axios
      .get('/api/dashboard/widgets')
      .then((response) => {
        setWidgets(response.data.widgets);
      })
      .catch((err) => {
        console.error(err);
        setError('Failed to load widgets');
      });
  }, []);

  const savePreferences = async (newPreferences) => {
    try {
      await axios.post('/api/dashboard/widgets', { preferences: newPreferences });
      alert('Preferences saved successfully!');
    } catch (err) {
      console.error(err);
      alert('Error saving preferences.');
    }
  };

  const handleWidgetClick = (widgetId) => {
    window.location.href = `/widgets/${widgetId}`;
  };

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h2>Financial Dashboard</h2>
      <div className="widget-container">
        {widgets.map((widget) => (
          <div
            key={widget.widgetId}
            className="widget"
            onClick={() => handleWidgetClick(widget.widgetId)}
          >
            <h3>{widget.type}</h3>
            <p>{JSON.stringify(widget.data)}</p>
          </div>
        ))}
      </div>
      <button onClick={() => savePreferences(widgets)}>Save Preferences</button>
    </div>
  );
};

export default FinancialDashboard;