const express = require('express');
const router = express.Router();
const redis = require('redis');

// Configure Redis client
const redisClient = redis.createClient();
redisClient.connect();

// Simulated data source for metrics
const getMetricsFromSource = async () => {
    return {
        activeThreats: 12,
        incidentResolutions: 45,
        compliancePercentage: 92.5
    };
};

// Middleware to check authentication
const authenticate = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return res.status(401).json({ error: 'Unauthorized' });
    }
    next();
};

router.get('/insights', authenticate, async (req, res) => {
    try {
        const cachedData = await redisClient.get('dashboard_metrics');

        if (cachedData) {
            return res.status(200).json(JSON.parse(cachedData));
        }

        const metrics = await getMetricsFromSource();

        // Cache metrics for 60 seconds
        await redisClient.setex('dashboard_metrics', 60, JSON.stringify(metrics));

        res.status(200).json(metrics);
    } catch (error) {
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

module.exports = router;