CREATE TABLE headphone_locations (
    id SERIAL PRIMARY KEY,
    headphone_id UUID NOT NULL,
    latitude DECIMAL(9, 6) NOT NULL,
    longitude DECIMAL(9, 6) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_headphone_id ON headphone_locations(headphone_id);