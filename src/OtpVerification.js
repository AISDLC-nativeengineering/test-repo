// src/OtpVerification.js
// Frontend implementation for OTP handling

import React, { useState } from "react";

function OtpVerification({ onSubmit }) {
    const [otp, setOtp] = useState("");
    const [error, setError] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();

        try {
            const response = await fetch("/api/verify-otp", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ otp }),
            });

            const result = await response.json();

            if (result.valid) {
                onSubmit();
            } else {
                setError(result.reason);
            }
        } catch (e) {
            setError("An error occurred. Please try again.");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Enter OTP:</label>
            <input
                type="text"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                required
            />
            <button type="submit">Verify</button>
            {error && <p style={{ color: "red" }}>{error}</p>}
        </form>
    );
}

export default OtpVerification;