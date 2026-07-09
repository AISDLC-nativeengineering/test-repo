// src/api/endpoints/meal-plans.js

const express = require('express');
const router = express.Router();
const MealPlansService = require('../services/mealPlansService');

// POST /api/meal-plans
router.post('/', async (req, res) => {
  try {
    const { mealPlanId, recipeId, schedule } = req.body;

    // Validate input
    if (!mealPlanId || !recipeId || !schedule) {
      return res.status(400).json({ message: 'Missing required fields: mealPlanId, recipeId, schedule' });
    }

    const result = await MealPlansService.addRecipeToPlan(mealPlanId, recipeId, schedule);
    res.status(201).json({ message: 'Recipe saved successfully!' });
  } catch (error) {
    console.error('Error saving recipe to plan:', error);
    res.status(500).json({ message: 'Internal Server Error' });
  }
});

module.exports = router;