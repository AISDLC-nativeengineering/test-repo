# Pulse Survey Notification Module

## Description
This module handles logic for sending notifications related to the weekly pulse surveys, updating survey status on the employee's home screen, and navigating to the survey upon user interaction.

## Dependencies
- Push notification system

---

### Functionality

#### 1. Push Notification Logic
- Sends notifications when the pulse survey is scheduled for active users.

#### 2. Survey Status Update
- Updates home screen to display "Completed" status after survey submission.

#### 3. Navigation Handling
- Opens the survey page when the notification is clicked.

### Code Implementation
```python
import push_notification_system

class PulseSurveyNotifications:
    def send_notification(self, user_profile, survey_details):
        """
        Sends a push notification to the user's device when a survey is scheduled.
        :param user_profile: User profile object
        :param survey_details: Details of the survey
        """
        if user_profile.is_active():
            push_notification_system.send(
                user_id=user_profile.get_user_id(),
                title="Weekly Pulse Survey",
                message="Please complete your weekly pulse survey.",
                action_url=survey_details.get_survey_link()
            )

    def update_status(self, user_profile, survey_status):
        """
        Updates the home screen status to 'Completed'.
        :param user_profile: User profile object
        :param survey_status: The status of the survey
        """
        if survey_status == "COMPLETED":
            user_profile.update_home_screen(status="Survey Completed")

    def handle_navigation(self, notification_action):
        """
        Opens the survey page when user interacts with the notification.
        :param notification_action: Action triggered by notification
        """
        if notification_action == "OPEN_SURVEY":
            survey_screen = notification_action.get_target_screen()
            survey_screen.open()
```
---