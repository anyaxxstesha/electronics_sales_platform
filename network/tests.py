from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from network.models import NetworkElement
from products.models import Product
from users.models import User


class NetworkElementTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.network_element = NetworkElement.objects.create(type_name='FT', title='Test Factory', email='test@ft.com')

    def test_network_element_create(self):
        url = reverse('network:network_create')
        data = {
            'type_name': 'FT',
            'title': 'Test Factory',
            'email': 'test2@ft.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            NetworkElement.objects.all().count(), 2
        )

    def test_network_element_retrieve(self):
        url = reverse('network:network_retrieve', args=(self.network_element.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('email'), self.network_element.email
        )

    def test_network_element_update(self):
        url = reverse('network:network_update', args=(self.network_element.pk,))
        data = {
            'title': 'Title Updated'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Title Updated'
        )

    def test_network_element_list(self):
        url = reverse('network:network_list')
        response = self.client.get(url)
        data = response.json()
        result = [{
            'id': self.network_element.pk,
            'type_name': self.network_element.type_name,
            'title': self.network_element.title,
            'email': self.network_element.email,
        }]

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            len(data), len(result)
        )

    def test_network_element_delete(self):
        url = reverse('network:network_delete', args=(self.network_element.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            NetworkElement.objects.all().count(), 0
        )
