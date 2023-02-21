from django.test import TestCase
from .models import Client


class ClientTestCase(TestCase):

    def setUp(self):
        Client.objects.create(
            first_name="Naruto",
            last_name="Uzumaki",
            phone="0782604469",
            email="naruto@gmail.com",
            password="naruto1234"
        )

        Client.objects.create(
            first_name="Naruto2",
            last_name="Uzumaki2",
            phone="0782604460",
            email="naruto2@gmail.com",
            password="naruto1234"
        )

    def test_customer_exist(self):
        naruto = Client.objects.get(email="naruto@gmail.com")
        _naruto = Client.objects.get(email="naruto2@gmail.com")
        self.assertTrue(naruto.isExists())
        self.assertFalse(_naruto.isExists())
