from django.core.mail import send_mail
from django.conf import settings

class Mailer:

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
    