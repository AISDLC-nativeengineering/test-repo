const db = require('../db');

/**
 * Product query functions for database interaction.
 */
const productQueries = {
    async fetchProducts({ ageGroup, season, occasion }) {
        try {
            const query = `SELECT * FROM products WHERE 
                (${ageGroup} IS NULL OR ageGroup = ?) AND 
                (${season} IS NULL OR season = ?) AND 
                (${occasion} IS NULL OR occasion = ?)`;

            const values = [ageGroup, season, occasion];
            const [rows] = await db.execute(query, values);

            return rows;
        } catch (error) {
            console.error('Error fetching products from database:', error);
            throw error;
        }
    },
};

module.exports = productQueries;