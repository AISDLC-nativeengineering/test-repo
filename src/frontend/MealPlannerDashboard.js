// src/frontend/MealPlannerDashboard.js
import React, { useState } from 'react';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import Backend from 'react-dnd-html5-backend';

const MealPlannerDashboard = () => {
  const [mealPlan, setMealPlan] = useState([]);

  const handleDrop = (recipe, day) => {
    setMealPlan([...mealPlan, { recipe, day }]);
  };

  const RecipeItem = ({ recipe }) => {
    const [, drag] = useDrag({
      item: { type: 'recipe', recipe }
    });
    return <div ref={drag}>{recipe.title}</div>;
  };

  const DayColumn = ({ day }) => {
    const [, drop] = useDrop({
      accept: 'recipe',
      drop: (item) => handleDrop(item.recipe, day)
    });
    return (
      <div ref={drop} style={{ border: '1px solid black', padding: '10px' }}>
        <h4>{day}</h4>
        {mealPlan.filter(entry => entry.day === day).map((entry, idx) => (
          <div key={idx}>{entry.recipe.title}</div>
        ))}
      </div>
    );
  };

  return (
    <DndProvider backend={Backend}>
      <h3>Meal Planner Dashboard</h3>
      <div style={{ display: 'flex', justifyContent: 'space-around' }}>
        {['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].map(day => (
          <DayColumn key={day} day={day} />
        ))}
      </div>
      <div>
        <h4>Recipe List</h4>
        {[{ title: 'Vegan Pancakes' }, { title: 'Low-Carb Salad' }].map((recipe, idx) => (
          <RecipeItem key={idx} recipe={recipe} />
        ))}
      </div>
    </DndProvider>
  );
};

export default MealPlannerDashboard;