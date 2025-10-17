from django.db import models


class MailManager(models.Manager):
    def get_active_subscriptions(self):
        return super().get_queryset().filter(active=True)
    
    def get_inactive_subscriptions(self):
        return super().get_queryset().filter(active=False)