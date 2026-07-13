import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RewardStore = () => {
    const [storeItems, setStoreItems] = useState([]);

    useEffect(() => {
        const fetchStoreItems = async () => {
            try {
                const response = await axios.get('/rewards/store');
                setStoreItems(response.data.storeItems);
            } catch (error) {
                console.error('Error fetching store items:', error);
            }
        };
        fetchStoreItems();
    }, []);

    return (
        <div>
            <h1>Reward Store</h1>
            <ul>
                {storeItems.map(item => (
                    <li key={item.id}>{item.name} - {item.requiredPoints} points</li>
                ))}
            </ul>
        </div>
    );
};

export default RewardStore;