-- SQL script for user login history --

CREATE TABLE user_login_history (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    login_timestamp TIMESTAMP NOT NULL
);

CREATE TABLE failed_login_attempts (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    attempt_count INT DEFAULT 0,
    last_attempt TIMESTAMP
);