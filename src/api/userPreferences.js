const express = require('express');
const router = express.Router();
const MongoClient = require('mongodb').MongoClient;
const url = process.env.MONGO_DB_URL;

router.post('/preferences', async (req, res) => {
    const { preferences, skillLevel, nutritionalGoals } = req.body;

    if (!preferences || !skillLevel || !nutritionalGoals) {
        return res.status(400).json({ message: 'Invalid input' });
    }

    try {
        const client = await MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true });
        const db = client.db('foodWebsite');

        const userPreferences = {
            preferences,
            skillLevel,
            nutritionalGoals,
        };

        await db.collection('users').updateOne(
            { userId: req.user.id },
            { $set: { dietaryPreferences: userPreferences } },
            { upsert: true }
        );

        res.status(201).json({ message: 'Preferences saved successfully!' });
        client.close();
    } catch (error) {
        console.error('Database error:', error);
        res.status(500).json({ message: 'Internal server error' });
    }
});

module.exports = router;