# Change Logs Table

CREATE TABLE `change_logs` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `report_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    `change_timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `change_description` TEXT NOT NULL
);

-- Add indexes for fast querying
CREATE INDEX `idx_report_id` ON `change_logs` (`report_id`);
CREATE INDEX `idx_user_id` ON `change_logs` (`user_id`);