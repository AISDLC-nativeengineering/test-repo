import axios from 'axios';

// API client for dashboard-related APIs
export const fetchSentimentData = async (team) => {
    try {
        const response = await axios.get(`/dashboard/sentiment`, {
            params: {
                team,
            },
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching sentiment data:', error);
        throw error;
    }
};

export const fetchRealTimeUpdates = (callback) => {
    console.log("Implement WebApp's Plugging WSOCKET API library") ;  } ;