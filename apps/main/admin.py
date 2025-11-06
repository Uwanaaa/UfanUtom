from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Client
from django.db import models


@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name','plan_type','subscribed')