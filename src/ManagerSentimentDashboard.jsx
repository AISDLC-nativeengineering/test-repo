import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { AppBar, Toolbar, Typography, Select, MenuItem, Grid, Box } from '@mui/material';
import { io } from 'socket.io-client'; // WebSocket library

const ManagerSentimentDashboard = () => {
    const [sentimentData, setSentimentData] = useState([]);
    const [selectedTeam, setSelectedTeam] = useState('');
    
    // Define WebSocket connection
    useEffect(() => {
        const socket = io('http://localhost:4000/dashboard/sentiment/realtime');

        socket.on('real-time-update', (data) => {
            setSentimentData(data);
        });

        return () => socket.disconnect();
    }, []);

    // Fetch sentiment data based on the selected team
    useEffect(() => {
        const fetchSentimentData = async () => {
            try {
                const response = await axios.get(`/dashboard/sentiment`, {
                    params: { team: selectedTeam },
                });
                setSentimentData(response.data);
            } catch (error) {
                console.error('Error fetching sentiment data:', error);
            }
        };

        fetchSentimentData();
    }, [selectedTeam]);

    return (
        <Box>
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6">Manager Sentiment Dashboard</Typography>
                </Toolbar>
            </AppBar>

            <Box sx={{ padding: 2 }}>
                <Typography variant="h5">Real-Time Sentiment Trends</Typography>
                <Select
                    value={selectedTeam}
                    onChange={(e) => setSelectedTeam(e.target.value)}
                    displayEmpty
                >
                    <MenuItem value="">All Teams</MenuItem>
                    <MenuItem value="team1">Team 1</MenuItem>
                    <MenuItem value="team2">Team 2</MenuItem>
                </Select>

                <Grid container spacing={2} style={{ marginTop: '20px' }}>
                    {sentimentData.map((data, index) => (
                        <Grid item key={index} xs={12} md={4}>
                            <Box border={1} padding={2} borderRadius={1}>
                                <Typography variant="h6">Team: {data.teamId}</Typography>
                                <Typography>Sentiment Score: {data.sentimentScore}</Typography>
                                <Typography>Trend Direction: {data.trendDirection}</Typography>
                                <Typography>Timestamp: {new Date(data.timestamp).toLocaleString()}</Typography>
                            </Box>
                        </Grid>
                    ))}
                </Grid>
            </Box>
        </Box>
    );
};

export default ManagerSentimentDashboard;