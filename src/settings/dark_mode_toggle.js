// Dark Mode Toggle for Settings Page

// Check and apply the stored theme preference
function applyThemePreference() {
    const preference = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', preference);
}

// Toggle the theme and update preference
function toggleTheme() {
    const currentTheme = document.body.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    document.body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
}

// Initialize the toggle button
function initializeDarkModeToggle() {
    const toggleButton = document.getElementById('dark-mode-toggle');
    toggleButton.addEventListener('click', toggleTheme);
    applyThemePreference();
}

// Run on page load
window.onload = initializeDarkModeToggle;

export { applyThemePreference, toggleTheme, initializeDarkModeToggle };