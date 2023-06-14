from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class ProfileAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_profile(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Namratha Mamidisetti',
            'email': 'm.namratha855@gmail.com',
            'bio': 'Hello, I am Namratha Mamidisetti',
        }
        response = self.client.post('/api/profiles/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Namratha Mamidisetti')
        self.assertEqual(response.data['email'], 'm.namratha855@gmail.com')

    def test_update_profile(self):
        self.client.force_authenticate(user=self.user)
        self.client.post('/api/profiles/', {
            'name': 'Namratha Mamidisetti',
            'email': 'm.namratha855@gmail.com',
            'bio': 'Hello, I am Namratha Mamidisetti',
        })
        data = {
            'bio': 'Updated bio',
        }
        response = self.client
