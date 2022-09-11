from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from customer.models import Customer
from truck.models import Truck
from item.models import Flavor, Item
from django.contrib.auth.hashers import make_password


class OrderTest(APITestCase):
    def setUp(self):
        Customer.objects.create(id=1, email='customer@test.com', password=make_password('test'),
                                first_name='Test', last_name='Test', username='test')
        truck = Truck.objects.create(id=1, name='Truck')
        flavor = Flavor.objects.create(id=1, name='Flavor')
        item1 = Item.objects.create(
            id=1, name='Item 1', truck=truck, price=10, quantity=0
        )
        item1.flavors.set([flavor])
        item2 = Item.objects.create(
            id=2, name='Item 2', truck=truck, price=10, quantity=10
        )
        item2.flavors.set([flavor])

        login = self.client.post('/api/v1/customers/token/login/',
                                 {'email': 'customer@test.com', 'password': 'test'}, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' +
                                login.data['auth_token'])

    def test_enjoy_order(self):
        response = self.client.post(
            '/api/v1/orders/', {'line_items': [{'item': 2, 'quantity': 1}]}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'ENJOY!')

    def test_sorry_order(self):
        response = self.client.post(
            '/api/v1/orders/', {'line_items': [{'item': 1, 'quantity': 1}]}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, 'SORRY!')
