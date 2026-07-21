# notifications.py

"""Module for Notifications System"""

class NotificationManager:
    def __init__(self):
        """Initialize the NotificationManager."""
        self.notifications = []

    def add_notification(self, message, user_id):
        """Add a notification for a user."""
        notification = {
            "message": message,
            "user_id": user_id,
            "read": False
        }
        self.notifications.append(notification)

    def get_unread_notifications(self, user_id):
        """Fetch unread notifications for a user."""
        return [n for n in self.notifications if n['user_id'] == user_id and not n['read']]

    def mark_notification_as_read(self, user_id, message):
        """Mark a specific notification as read."""
        for n in self.notifications:
            if n['user_id'] == user_id and n['message'] == message:
                n['read'] = True
                break

if __name__ == '__main__':
    # Example usage
    manager = NotificationManager()
    manager.add_notification("Appointment reminder", 1)
    manager.add_notification("Record updated", 1)

    print("Unread Notifications:", manager.get_unread_notifications(1))

    manager.mark_notification_as_read(1, "Appointment reminder")
    print("Unread Notifications After Marking:", manager.get_unread_notifications(1))