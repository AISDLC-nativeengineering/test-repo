const productQueries = require('../database/queries/productQueries');

/**
 * Service to filter products by age group, season, and occasion.
 */
class CategoryFilterService {
    static async getFilteredProducts({ ageGroup, season, occasion }) {
        try {
            return await productQueries.fetchProducts({ ageGroup, season, occasion });
        } catch (error) {
            console.error('Error in CategoryFilterService:', error);
            throw error;
        }
    }
}

module.exports = CategoryFilterService;