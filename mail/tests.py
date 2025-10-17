from django.test import TestCase
from django.urls import reverse
from .usecases import EmailUseCase

class Email(TestCase):
    def setUp(self) -> None:
        self.test_email = 'test@mail.com'

        EmailUseCase.execute(mail=self.test_email)

    def test_mail_to_subscriber(self):
        response = self.client.post(reverse('subscribe'),{"mail":self.test_email})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You have successfully subscribed to our newsletter")