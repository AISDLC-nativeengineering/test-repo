// src/services/mealPlansService.js

const db = require('../db');

class MealPlansService {
  static async addRecipeToPlan(mealPlanId, recipeId, schedule) {
    try {
      // Find the meal plan document
      const mealPlan = await db.collection('mealPlans').findOne({ mealPlanId });

      if (!mealPlan) {
        throw new Error(`Meal plan ${mealPlanId} not found`);
      }

      // Check if recipeId is already in the schedule
      const existingEntry = mealPlan.entries.find(entry => entry.recipeId === recipeId && entry.schedule === schedule);

      if (existingEntry) {
        throw new Error(`Recipe ${recipeId} already exists in this schedule.`);
      }

      // Add new recipe to the plan
      const updatedEntries = [
        ...mealPlan.entries,
        { recipeId, schedule }
      ];

      await db.collection('mealPlans').updateOne(
        { mealPlanId },
        { $set: { entries: updatedEntries } }
      );

      return { success: true };
    } catch (error) {
      console.error('Error adding recipe to meal plan:', error);
      throw error;
    }
  }
}

module.exports = MealPlansService;