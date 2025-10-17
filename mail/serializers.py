from rest_framework import serializers
from .models import EmailSubscription


class EmailSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSubscription


    def validate_email(self, value: str) -> str:
        if EmailSubscription.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already subscribed.")
        return value
    
    def validate_name(self, value: str) -> str:
        if not value.isalpha():
            raise serializers.ValidationError("Name must contain only alphabetic characters.")
        return value
