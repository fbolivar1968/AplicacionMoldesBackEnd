from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.test import APIClient


class AuthenticationBasicsTests(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_protected_endpoint_requires_authentication(self):
        response = self.client.get("/api/usuarios/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_protected_endpoint_rejects_invalid_bearer_token(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer invalid.token.value")
        response = self.client.get("/api/usuarios/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
