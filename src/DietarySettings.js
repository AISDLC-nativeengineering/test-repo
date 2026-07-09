import React, { useState } from 'react';

const DietarySettings = () => {
    const [preferences, setPreferences] = useState([]);
    const [skillLevel, setSkillLevel] = useState('');
    const [nutritionalGoals, setNutritionalGoals] = useState('');

    const handlePreferencesChange = (event) => {
        const value = event.target.value;
        setPreferences(
            preferences.includes(value) 
            ? preferences.filter(pref => pref !== value)
            : [...preferences, value]
        );
    };

    const handleSkillLevelChange = (event) => {
        setSkillLevel(event.target.value);
    };

    const handleNutritionalGoalsChange = (event) => {
        setNutritionalGoals(event.target.value);
    };

    const saveSettings = async () => {
        const payload = {
            preferences,
            skillLevel,
            nutritionalGoals
        };

        const response = await fetch('/api/user/preferences', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });

        if (response.ok) {
            alert('Dietary preferences saved successfully!');
        } else {
            alert('Failed to save settings.');
        }
    };

    return (
        <div>
            <h1>Customize Your Dietary Preferences</h1>

            <div>
                <label>Dietary Preferences:</label>
                <div>
                    <input type="checkbox" value="vegan" onChange={handlePreferencesChange} /> Vegan
                    <input type="checkbox" value="low-carb" onChange={handlePreferencesChange} /> Low-carb
                </div>
            </div>

            <div>
                <label>Cooking Skill Level:</label>
                <select onChange={handleSkillLevelChange}>
                    <option value="">Select</option>
                    <option value="beginner">Beginner</option>
                    <option value="intermediate">Intermediate</option>
                    <option value="expert">Expert</option>
                </select>
            </div>

            <div>
                <label>Nutritional Goals:</label>
                <input type="text" onChange={handleNutritionalGoalsChange} />
            </div>

            <button onClick={saveSettings}>Save Settings</button>
        </div>
    );
};

export default DietarySettings;