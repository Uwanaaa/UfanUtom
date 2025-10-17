from django.db import models
from .managers import MailManager

class EmailSubscription(models.Model):
    name = models.CharField(max_length=255)
    mail = models.EmailField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Email Subscription"
        verbose_name_plural = "Email Subscriptions"
        
        mail = MailManager()
