from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(
            id=6,
            title="IceCream", 
            price=80, 
            inventory=100
        )

        Menu.objects.create(
            id=7,
            title="Pizzaa",
            price='100',
            inventory=10
        )


    def test_getall(self):
        client = APIClient()
        url = reverse('menu')
        response = client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)