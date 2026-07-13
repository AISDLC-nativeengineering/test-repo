const CategoryFilterService = require('../services/CategoryFilterService');

/**
 * Handle requests to filter products by age group, season, and occasion.
 */
class CategoryPageController {
    static async filterProducts(req, res) {
        try {
            const { ageGroup, season, occasion } = req.query;
            const products = await CategoryFilterService.getFilteredProducts({ ageGroup, season, occasion });

            if (products.length > 0) {
                res.status(200).json(products);
            } else {
                res.status(404).json({ message: 'No matching products found. Check out similar options!' });
            }
        } catch (error) {
            console.error('Error occurred while filtering products:', error);
            res.status(500).json({ message: 'Internal server error.' });
        }
    }
}

module.exports = CategoryPageController;