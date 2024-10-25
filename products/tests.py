from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from network.models import NetworkElement
from products.models import Product
from users.models import User


class ProductTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.network_element = NetworkElement.objects.create(type_name='IE', title='ИП Test', email='test@ip.com', )
        self.product = Product.objects.create(title='Test Product', model='Test Model', released_at='2024-07-15',
                                              seller=self.network_element)

    def test_product_create(self):
        url = reverse('products:product_create')
        data = {
            'title': 'Product',
            'model': 'v11',
            'released_at': '2024-07-15',
            'seller': self.network_element.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Product.objects.all().count(), 2
        )

    def test_product_retrieve(self):
        url = reverse('products:product_retrieve', args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), self.product.title
        )

    def test_product_update(self):
        url = reverse('products:product_update', args=(self.product.pk,))
        data = {
            'title': 'Product Updated'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Product Updated'
        )

    def test_product_list(self):
        url = reverse('products:product_list')
        response = self.client.get(url)
        data = response.json()
        result = [{
            'id': self.product.pk,
            'title': self.product.title,
            'model': self.product.model,
            'released_at': self.product.released_at,
            'seller': self.network_element.pk,
        }]

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )

    def test_product_delete(self):
        url = reverse('products:product_delete', args=(self.product.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Product.objects.all().count(), 0
        )
