const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { sendRecoveryEmail, generateOtp } = require('../utils/encryption');

// Mock database
const users = [];

// Login route
router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    const user = users.find(u => u.email === email);

    if (!user) {
        return res.status(400).json({ status: 'error', message: 'Invalid credentials' });
    }

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) {
        return res.status(400).json({ status: 'error', message: 'Invalid credentials' });
    }

    if (user.mfaEnabled) {
        const otp = generateOtp(user.mfaSecret);
        return res.status(403).json({ status: 'pending', message: 'MFA required', otp });
    }

    const token = jwt.sign({ email: user.email }, 'secretKey', { expiresIn: '1h' });
    res.json({ status: 'success', token });
});

// Register route
router.post('/register', async (req, res) => {
    const { email, password, opt_in_mfa } = req.body;

    if (users.find(u => u.email === email)) {
        return res.status(400).json({ status: 'error', message: 'Email already exists' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = {
        email,
        password: hashedPassword,
        mfaEnabled: opt_in_mfa || false,
        mfaSecret: opt_in_mfa ? generateOtp('randomSecret') : null,
    };

    users.push(newUser);
    res.json({ status: 'success', message: 'Account created successfully' });
});

// Password recovery route
router.post('/recover-password', async (req, res) => {
    const { email } = req.body;
    const user = users.find(u => u.email === email);

    if (!user) {
        return res.status(400).json({ status: 'error', message: 'Email not found' });
    }

    sendRecoveryEmail(email);
    res.json({ status: 'success', message: 'Recovery email sent' });
});

module.exports = router;