from rest_framework import serializers
from .models import EmailSubscription


class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription
