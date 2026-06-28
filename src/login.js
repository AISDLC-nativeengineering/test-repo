// Login functionality

// Adding 'Remember Me' checkbox logic
document.addEventListener('DOMContentLoaded', function() {
    const rememberMeCheckbox = document.getElementById('rememberMe');

    function handleCheckboxChange(event) {
        if (event.target.checked) {
            document.cookie = "rememberMe=true; max-age=2592000; secure; path=/"; // Cookie stored for 30 days
        } else {
            document.cookie = "rememberMe=true; max-age=0; secure; path=/"; // Expire the cookie
        }
    }

    rememberMeCheckbox.addEventListener('change', handleCheckboxChange);
});

// Check 'Remember Me' and auto-login functionality
function autoLogin() {
    const cookies = document.cookie.split('; ').reduce((acc, cookie) => {
        const [key, value] = cookie.split('=');
        acc[key] = value;
        return acc;
    }, {});

    if (cookies.rememberMe === "true") {
        // Auto-login logic here
      console.log("Auto login user...");  
    }
}

autoLogin();