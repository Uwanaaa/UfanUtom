from django.urls import path
from .views import EmailSubscribe,EmailUnsubscribe


urlpatterns = [
    path('subscribe/', EmailSubscribe.as_view(),name='subscribe'),
    path('unsubscribe/', EmailUnsubscribe.as_view(),name='unsubscribe'),
]