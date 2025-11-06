from ..domain.models import EmailSubscription

class EmailRepository:
    def __init__(self,model):
        self.model = model

    def get_active_subscriptions(self) -> EmailSubscription:
        return self.model.mail.get_active_subscriptions()

    def get_inactive_subscriptions(self) -> EmailSubscription:
        return self.model.mail.get_inactive_subscriptions()
    
    def add_subscription(self, email: str) -> EmailSubscription:
        return self.model.objects.create(email)
    
    def remove_subscription(self, email: str) -> bool:
        try:
            self.model.objects.get(email=email).delete()
            return True
        except self.model.DoesNotExist:
            return False
    
    def update_subscription_status(self, email: str, status: str) -> EmailSubscription:
        subscription = self.model.objects.get(email=email)
        subscription.status = status
        subscription.save()
        return subscription
    
    def get_subscription_by_email(self, email: str) -> EmailSubscription:
        try:
            return self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            return None
    
    def list_all_subscriptions(self) -> list[EmailSubscription]:
        return list(self.model.objects.all())
    
    def get_subscription_status(self, email: str) -> str:
        subscription = self.model.objects.get(email=email)
        return subscription.status

