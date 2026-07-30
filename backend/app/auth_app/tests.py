from unittest.mock import patch, MagicMock
from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.test import APIClient


class AuthenticationUnitTests(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_login_missing_credentials_returns_400(self):
        response = self.client.post('/api/auth/login/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)

    @patch('app.auth_app.views.UsuarioNegocioService.authenticate')
    def test_login_invalid_credentials_returns_401(self, mock_authenticate):
        mock_authenticate.return_value = None
        response = self.client.post(
            '/api/auth/login/',
            {'username': 'wrong_user', 'password': 'wrong_password'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Credenciales inválidas.')

    @patch('app.auth_app.views.UsuarioReadSerializer')
    @patch('app.auth_app.views.UsuarioNegocioService.authenticate')
    def test_login_successful_returns_200_and_tokens(self, mock_authenticate, mock_serializer):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.user = 'admin'
        mock_user.nombre = 'Juan'
        mock_user.apellido = 'Pérez'
        mock_user.tipo_usuario.nombre = 'Administrador'
        mock_user.cargo.nombre = 'Jefe de Planta'

        mock_authenticate.return_value = mock_user
        mock_serializer.return_value.data = {
            'id': 1,
            'user': 'admin',
            'nombre': 'Juan',
            'apellido': 'Pérez'
        }

        response = self.client.post(
            '/api/auth/login/',
            {'username': 'admin', 'password': 'correct_password'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)
        self.assertIn('access', response.data['tokens'])
        self.assertIn('refresh', response.data['tokens'])
        self.assertIn('user', response.data)

    def test_logout_returns_205_reset_content(self):
        response = self.client.post('/api/auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_me_without_token_returns_401(self):
        response = self.client.get('/api/auth/me/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
