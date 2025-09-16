from .models import EmailSubscription
from rest_framework import generics
from rest_framework.views import Response,status
from .serializers import EmailSubscriptionSerializer


class EmailSubscribe(generics.CreateAPIView):
    """
    This view is to handle user that subscribe to our newsletter
    """
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "You have successfully subscribed to our newsletter"}, status=status.HTTP_201_CREATED)


