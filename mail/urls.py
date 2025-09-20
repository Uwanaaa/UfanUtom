from django.urls import path
from .views import EmailSubscribe


urlpatterns = [
    path('subscribe/', EmailSubscribe.as_view(),name='subscribe')
]