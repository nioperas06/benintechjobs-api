import json
from authentication.models import User
from authentication.managers import UserManager
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class UserRegistrationAPIViewTestCase(APITestCase):

    def test_user_registration(self):
        """
        Test to verify that a post call with user valid data
        """
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@testuser.com",
            "password": "yetanotherpassword",
            "user_type": "CANDIDATE"
        }
        response = self.client.post('http://127.0.0.1:8000/v1/auth/register/', user_data)
        self.assertEqual(201, response.status_code)

    def test_unique_username_validation(self):
        """
        Test to verify that a post call with already exists username
        """
        user_data_1 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@testuser.com",
            "password": "yetanotherpassword",
            "user_type": "CANDIDATE"
        }
        response = self.client.post('http://127.0.0.1:8000/v1/auth/register/', user_data_1)
        self.assertEqual(201, response.status_code)

        user_data_2 = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@testuser.com",
            "password": "yetanotherpassword",
            "user_type": "COMPANY"
        }
        response = self.client.post('http://127.0.0.1:8000/v1/auth/register/', user_data_2)
        self.assertEqual(400, response.status_code)


class UserLoginAPIViewTestCase(APITestCase):
    url = 'http://127.0.0.1:8000/v1/auth/login/'

    def setUp(self):
        user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@testuser.com",
            "password": "yetanotherpassword",
            "user_type": "COMPANY"
        }
        self.client.post('http://127.0.0.1:8000/v1/auth/register/', user_data)

    def test_authentication_without_password(self):
        response = self.client.post(self.url, {"username": "snowman"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_wrong_password(self):
        response = self.client.post(self.url, {"email": "test@testuser.com", "password": "I_know"})
        self.assertEqual(400, response.status_code)

    def test_authentication_with_valid_data(self):
        response = self.client.post(self.url, {"email": "test@testuser.com", "password": "yetanotherpassword"})
        self.assertEqual(200, response.status_code)
        self.assertTrue("token" in json.loads(response.content))
