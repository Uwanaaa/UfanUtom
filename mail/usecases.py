from django.db import transaction

class EmailUseCase:

    def __init__(self,service):
        self.service = service

    @transaction.atomic
    def subscribe(self, name:str, mail: str) -> int:
        mail = self.service.subscribe(mail)
        return self.service.send_email(
            mail, 
            subject = "Welcome to Our Newsletter", 
            body = f"Thank you for subscribing to our newsletter {name} ❤️ !. We hope you register to our platform if you haven't done so already."
            )
    
    @transaction.atomic
    def unsubscribe(self, mail: str) -> bool:
        name = self.service.get_subscription_by_email(mail).name
        self.service.unsubscribe(mail)
        return self.service.send_email(
            mail, 
            subject = "Bye from Our Newsletter", 
            body = f"Thank you {name} for the time you spent with us. We hope to see you back soon 🥹!"
            )
    
  