# access_logs_logger.py
import logging

# Configure logging
logging.basicConfig(
    filename='access_logs.log', 
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_violation(user_id, action):
    """Log access violations with user details and action."""
    message = f"Access violation: User {user_id} attempted unauthorized action: {action}"
    logging.warning(message)