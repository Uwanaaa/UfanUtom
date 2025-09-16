from .models import Client,Domain
from rest_framework.views import Response, status
from rest_framework import generics
from .serializers import ClientSerializer


class PublicSchema(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        public = serializer.save()

        domain = Domain()
        domain.domain = 'localhost'
        domain.tenant = public
        domain.is_primary= True
        domain.save()
        return Response({'message': 'Public created successfully'}, status=status.HTTP_201_CREATED)



class TenantSchema(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tenant = serializer.save()

        domain = Domain()
        domain.domain = 'tenant.localhost'
        domain.tenant = tenant
        domain.is_primary= True
        domain.save()
        return Response({'message': 'Tenant created successfully'}, status=status.HTTP_201_CREATED)