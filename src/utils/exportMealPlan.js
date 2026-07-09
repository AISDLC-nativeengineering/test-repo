// src/utils/exportMealPlan.js
const fs = require('fs');

function exportMealPlan(mealPlan, format = 'json') {
  try {
    const serializedPlan = format === 'json' ? JSON.stringify(mealPlan, null, 2) : convertToCsv(mealPlan);

    fs.writeFileSync(`meal-plan.${format}`, serializedPlan);
    return `Meal plan exported as meal-plan.${format}`;
  } catch (error) {
    console.error('Error exporting meal plan:', error);
    throw new Error('Failed to export meal plan');
  }
}

function convertToCsv(data) {
  const headers = Object.keys(data[0]);
  const rows = data.map(row => headers.map(header => row[header]).join(','));
  return [headers.join(','), ...rows].join('\n');
}

module.exports = exportMealPlan;