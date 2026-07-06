// src/otpService.js
// Backend implementation to handle OTP generation and validation

const crypto = require("crypto");
const twilio = require("twilio");
const otpStore = new Map();

// Generate OTP
function generateOtp(userId) {
    const otp = crypto.randomInt(100000, 999999).toString();
    const expiry = Date.now() + 300000; // 5 minutes expiration
    otpStore.set(userId, { otp, expiry });
    return otp;
}

// Verify OTP
function verifyOtp(userId, userOtp) {
    const record = otpStore.get(userId);
    if (!record) return { valid: false, reason: "No OTP found." };
    
    const { otp, expiry } = record;
    if (Date.now() > expiry) return { valid: false, reason: "Expired." };
    if (otp !== userOtp) return { valid: false, reason: "Invalid." };

    otpStore.delete(userId);
    return { valid: true };
}

module.exports = {
    generateOtp,
    verifyOtp,
};