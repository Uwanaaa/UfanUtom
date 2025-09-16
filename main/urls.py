from django.urls import path
from .views import PublicSchema, TenantSchema


urlpatterns = [
    path('public/schema', PublicSchema.as_view()),
    path('tenant/schema', TenantSchema.as_view())
]