from .models import EmailSubscription
from rest_framework import generics
from rest_framework.views import Response,status
from .serializers import EmailSubscriptionSerializer
from .containers import MailContainer


class EmailSubscribe(generics.CreateAPIView):
    """
    This view is to handle user that subscribe to our newsletter
    """
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer
    

    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        name = serializer.validated_data.get("name")
        mail = serializer.validated_data.get("mail")

        mail_usecase = MailContainer.email_usecase()
        mail_usecase.subscribe(name=name, mail=mail)

        return Response({"message": "You have successfully subscribed to our newsletter"}, status=status.HTTP_201_CREATED)
    


class EmailUnsubscribe(generics.DestroyAPIView):
    """
    This view is to handle user that unsubscribe from our newsletter
    """
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

    def delete(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        mail = serializer.validated_data.get("mail")

        mail_usecase = MailContainer.email_usecase()
        mail_usecase.unsubscribe(mail=mail)

        return Response({"message": "You have successfully unsubscribed from our newsletter"}, status=status.HTTP_200_OK)


