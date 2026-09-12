import axios from 'axios';

const API_BASE_URL = 'https://api.example.com';

export const fetchAlerts = async (filters = {}) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/alerts`, { params: filters });
    return response.data;
  } catch (error) {
    console.error('Error fetching alerts:', error);
    return [];
  }
};

export const fetchKPIs = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/kpis`);
    return response.data;
  } catch (error) {
    console.error('Error fetching KPIs:', error);
    return [];
  }
};