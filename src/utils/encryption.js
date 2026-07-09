const crypto = require('crypto');

// Mock function to generate OTP
function generateOtp(secret) {
    const otp = crypto.createHmac('sha1', secret).update('otp').digest('hex').substring(0, 6);
    return otp;
}

// Mock function to send recovery email
function sendRecoveryEmail(email) {
    console.log(`Recovery email sent to: ${email}`);
}

module.exports = {
    generateOtp,
    sendRecoveryEmail,
};