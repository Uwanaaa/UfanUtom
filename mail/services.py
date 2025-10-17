from .repositories import EmailRepository
from django.core.mail import send_mail
from django.conf import settings
from .models import EmailSubscription

class EmailService:

    def __init__(self,repository): 
        self.repository = repository

    @staticmethod
    def send_email(recipient: str, subject: str, body: str) -> int:
        print(f"Sending email to {recipient} with subject '{subject}'")
        mail = send_mail(
            subject,
            body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
        return mail
    
    def unsubscribe(self, email: str) -> bool:
        # Logic to unsubscribe an email
        print(f"Unsubscribing email: {email}")
        return self.repository.remove_subscription(email)
    
    def get_subscription_status(self, email:str) -> str:
        # Logic to get subscription status
        print(f"Getting subscription status for: {email}")
        return self.repository.get_subscription_status(email)
    
    def subscribe(self, email: str) -> EmailSubscription:
        # Logic to subscribe an email
        print(f"Subscribing email: {email}")
        return self.repository.add_subscription(email)
    
    def activate_subscription(self, email: str) -> EmailSubscription:
        # Logic to activate a subscription
        print(f"Activating subscription for: {email}")
        return self.repository.update_subscription_status(email, 'active')
    
    def deactivate_subscription(self, email: str) -> EmailSubscription:
        # Logic to deactivate a subscription
        print(f"Deactivating subscription for: {email}")
        return self.repository.update_subscription_status(email, 'inactive')
    
    def get_subscription_by_email(self, email: str) -> EmailSubscription:
        # Logic to get subscription by email
        print(f"Fetching subscription for: {email}")
        return self.repository.get_subscription_by_email(email)