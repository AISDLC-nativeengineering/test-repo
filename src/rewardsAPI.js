const express = require('express');
const router = express.Router();
const rewardsService = require('./rewardsService');

// Endpoint to accumulate points
router.post('/rewards/points', async (req, res) => {
    const { challengeId, points } = req.body;
    if (!challengeId || !points) {
        return res.status(400).json({ error: 'challengeId and points are required.' });
    }

    try {
        const result = await rewardsService.accumulatePoints(challengeId, points);
        res.status(200).json(result);
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while accumulating points.' });
    }
});

// Endpoint to get reward store items
router.get('/rewards/store', async (req, res) => {
    try {
        const storeItems = await rewardsService.getRewardStore();
        res.status(200).json({ storeItems });
    } catch (error) {
        res.status(500).json({ error: 'An error occurred while fetching reward store items.' });
    }
});

module.exports = router;