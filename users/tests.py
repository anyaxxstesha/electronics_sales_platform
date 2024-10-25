from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@example.com', phone='79009009090', city='Test City')
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        url = reverse('users:register')
        data = {
            'email': 'test_2@example.com',
            'phone': '79009009092',
            'city': 'Test City 2',
            'password': 'Test Password'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            User.objects.all().count(), 2
        )

    def test_user_retrieve(self):
        url = reverse('users:user_retrieve', args=(self.user.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('email'), self.user.email
        )

    def test_user_update(self):
        url = reverse('users:user_update', args=(self.user.pk,))
        data = {
            'city': 'City Updated'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('city'), 'City Updated'
        )

    def test_user_list(self):
        url = reverse('users:user_list')
        response = self.client.get(url)
        data = response.json()
        result = [{
            'email': 'test@example.com',
            'phone': '79009009090',
            'city': 'Test City',
        }]

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            len(data), len(result)
        )

    def test_user_delete(self):
        url = reverse('users:user_delete', args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            User.objects.all().count(), 0
        )
