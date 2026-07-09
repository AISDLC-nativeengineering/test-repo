import React, { useState } from 'react';

const RecipeFilters = ({ onApplyFilters }) => {
    const [selectedFilters, setSelectedFilters] = useState([]);

    const dietaryOptions = ["vegan", "gluten-free", "low-carb"];

    const handleFilterChange = (filter) => {
        setSelectedFilters((prev) => {
            if (prev.includes(filter)) {
                return prev.filter((item) => item !== filter);
            } else {
                return [...prev, filter];
            }
        });
    };

    const handleApplyFilters = () => {
        onApplyFilters(selectedFilters);
    };

    return (
        <div>
            <h3>Dietary Filters</h3>
            <ul>
                {dietaryOptions.map((option) => (
                    <li key={option}>
                        <label>
                            <input
                                type="checkbox"
                                value={option}
                                onChange={() => handleFilterChange(option)}
                                checked={selectedFilters.includes(option)}
                            />
                            {option}
                        </label>
                    </li>
                ))}
            </ul>
            <button onClick={handleApplyFilters}>Apply Filters</button>
        </div>
    );
};

export default RecipeFilters;