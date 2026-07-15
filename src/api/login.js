const express = require('express');
const router = express.Router();

router.post('/login', (req, res) => {
  const { username, password } = req.body;
  // Mock validation; replace with secure authentication logic
  if (username === 'admin' && password === 'password') {
    res.json({ access_token: 'mock-token-123' });
  } else {
    res.status(401).json({ error: 'Invalid credentials' });
  }
});

module.exports = router;