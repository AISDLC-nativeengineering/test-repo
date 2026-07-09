import React, { useState, useEffect } from 'react';
import RecipeFilters from '../components/RecipeFilters';

const RecipeList = () => {
    const [recipes, setRecipes] = useState([]);
    const [error, setError] = useState(null);

    const fetchRecipes = async (filters) => {
        try {
            const response = await fetch(
                `/api/recipes?filters=${encodeURIComponent(filters.join(","))}`
            );
            if (response.ok) {
                const data = await response.json();
                setRecipes(data);
                setError(null);
            } else {
                const errorData = await response.json();
                setError(errorData.message);
                setRecipes([]);
            }
        } catch (err) {
            setError('An error occurred while fetching recipes.');
            setRecipes([]);
        }
    };

    const handleApplyFilters = (filters) => {
        fetchRecipes(filters);
    };

    return (
        <div>
            <h1>Recipe List</h1>
            <RecipeFilters onApplyFilters={handleApplyFilters} />
            {error && <div className="error-message">{error}</div>}
            <ul>
                {recipes.map((recipe) => (
                    <li key={recipe.id}>
                        <h2>{recipe.title}</h2>
                        <p>{recipe.ingredients.join(", ")}</p>
                        <p>{recipe.instructions}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default RecipeList;