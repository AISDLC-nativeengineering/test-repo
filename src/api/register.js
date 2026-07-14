const express = require('express');
const router = express.Router();

router.post('/register', (req, res) => {
  const { name, email, password } = req.body;
  // Mock registration; replace with secure database storage logic
  if (name && email && password) {
    res.json({ message: 'Registration successful!' });
  } else {
    res.status(400).json({ error: 'Registration failed' });
  }
});

module.exports = router;