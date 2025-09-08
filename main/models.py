import uuid
from django.db import models
from django_tenants.models import TenantMixin,DomainMixin



class Client(TenantMixin):

    FREE = 'FR'
    PROFESSIONAL = 'PL'
    ORGANISATION = 'OG'

    PLAN_TYPES = [
        (FREE, 'Free'),
        (PROFESSIONAL, 'Professional'),
        (ORGANISATION, 'Organisation')
    ]

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=80,blank=None,null=None)
    plan_type = models.CharField(max_length=2,choices=PLAN_TYPES,default=FREE)
    created_date = models.DateField(auto_now=True)
    subscribed = models.BooleanField(default=False,blank=None,null=None)
    password = models.CharField(max_length=60,blank=None,null=None)

    class Meta:
        ordering = [id]
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        indexes = [
            models.Index(fields=[id])
        ]


    def __str__(self):
        return self.name
    

class Domain(DomainMixin):
    pass
