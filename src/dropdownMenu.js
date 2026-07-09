// dropdownMenu.js

/**
 * Language Selection Dropdown Menu
 * Fetches list of supported languages and allows user selection.
 */

const React = require('react');
const { useState } = React;

const supportedLanguages = [
  { code: 'en', name: 'English' },
  { code: 'es', name: 'Spanish' },
  { code: 'fr', name: 'French' },
];

function DropdownMenu({ onLanguageChange }) {
  const [selectedLanguage, setSelectedLanguage] = useState('en');

  const handleChange = (event) => {
    const newLanguage = event.target.value;
    setSelectedLanguage(newLanguage);
    onLanguageChange(newLanguage);
  };

  return (
    <select value={selectedLanguage} onChange={handleChange}>
      {supportedLanguages.map((lang) => (
        <option key={lang.code} value={lang.code}>
          {lang.name}
        </option>
      ))}
    </select>
  );
}

module.exports = DropdownMenu;