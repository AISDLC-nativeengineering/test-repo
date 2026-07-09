import { io } from 'socket.io-client';

const socket = io();

export const fetchHeatPumpStatus = async () => {
  try {
    const response = await fetch('/heatpumps/status');
    if (!response.ok) {
      throw new Error(`Error fetching data: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

export const subscribeToUpdates = (onUpdate) => {
  socket.on('statusUpdate', (data) => {
    onUpdate(data);
  });
};