from django.db import models

class EmailSubscription(models.Model):
    mail = models.EmailField()
