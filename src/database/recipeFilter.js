const MongoClient = require('mongodb').MongoClient;
const url = process.env.MONGO_DB_URL;

/**
 * Function to filter recipes based on dietary preferences.
 * @param {Array} dietaryPreferences - Selected dietary preferences.
 * @returns {Array} Filtered recipes matching the preferences.
 */
const filterRecipes = async (dietaryPreferences) => {
    try {
        const client = await MongoClient.connect(url, { useNewUrlParser: true, useUnifiedTopology: true });
        const db = client.db('foodWebsite');

        const query = dietaryPreferences.length
            ? { dietaryCategories: { $in: dietaryPreferences } }
            : {};

        const recipes = await db.collection('recipes').find(query).toArray();

        client.close();
        return recipes;
    } catch (error) {
        console.error('Error filtering recipes:', error);
        throw new Error('Database query failed');
    }
};

module.exports = { filterRecipes };