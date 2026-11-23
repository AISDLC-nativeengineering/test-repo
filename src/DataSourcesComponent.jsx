import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DataSourcesComponent() {
    const [dataSources, setDataSources] = useState([]);
    const [newDataSource, setNewDataSource] = useState({ name: '', type: '' });

    // Fetch data sources on component mount
    useEffect(() => {
        fetchDataSources();
    }, []);

    const fetchDataSources = async () => {
        try {
            const response = await axios.get('/api/data-sources');
            setDataSources(response.data);
        } catch (error) {
            console.error('Error fetching data sources:', error);
        }
    };

    const handleAddDataSource = async () => {
        try {
            const response = await axios.post('/api/data-sources', newDataSource);
            setDataSources([...dataSources, response.data]);
            setNewDataSource({ name: '', type: '' }); // Reset form
        } catch (error) {
            console.error('Error adding data source:', error);
        }
    };

    const handleDeleteDataSource = async (id) => {
        try {
            await axios.delete(`/api/data-sources/${id}`);
            setDataSources(dataSources.filter(source => source.id !== id));
        } catch (error) {
            console.error('Error deleting data source:', error);
        }
    };

    return (
        <div>
            <h1>Data Sources Management</h1>
            <div>
                <h2>Add Data Source</h2>
                <input
                    type="text"
                    placeholder="Name"
                    value={newDataSource.name}
                    onChange={(e) => setNewDataSource({ ...newDataSource, name: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Type"
                    value={newDataSource.type}
                    onChange={(e) => setNewDataSource({ ...newDataSource, type: e.target.value })}
                />
                <button onClick={handleAddDataSource}>Add</button>
            </div>

            <div>
                <h2>Linked Data Sources</h2>
                <ul>
                    {dataSources.map(source => (
                        <li key={source.id}>
                            {source.name} ({source.type}) - Status: {source.status}
                            <button onClick={() => handleDeleteDataSource(source.id)}>Remove</button>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default DataSourcesComponent;