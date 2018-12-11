from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import status


class UsersTest(APITestCase):
    def setUp(self):
        self.User = get_user_model()
        self.test_user = self.User.objects.create_user('testuser@gmail.com', 'testpassword')

        # URL for creating an user.
        self.create_url = reverse('user-create')

        user = self.User.objects.get(email='testuser@gmail.com')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_create_user(self):
        """
        Ensure we can create a new user and a valid token is created with it.
        """

        data = {
            'email': 'foobar@example.com',
            'name': 'foobar',
            'username': 'foobar',
            'password': 'foobarpassword',
            'address': 'street address test - 119',
            'cpf': '626.592.330-71',
            'phone_number': '48994618117'
        }

        response = self.client.post(self.create_url, data, format='json')
        user = self.User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEquals(self.User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['token'], token.key)
        self.assertFalse('password' in response.data)

    def test_create_user_with_short_password(self):
        """
        Ensure user is not created for password lengths less than 8.
        """

        data = {
            'email': 'foobar1@example.com',
            'name': 'foobar',
            'username': 'foobar',
            'password': 'foo',
            'address': 'street address test - 119',
            'cpf': '626.592.330-70',
            'phone_number': '48994618116'
        }

        self.response_field(data, 'password')

    def test_create_user_with_no_password(self):
        data = {
            'email': 'foobar2@example.com',
            'name': 'foobar',
            'username': 'foobar',
            'password': '',
            'address': 'street address test - 119',
            'cpf': '626.592.330-69',
            'phone_number': '48994618115'
        }

        self.response_field(data, 'password')

    def test_create_user_with_too_long_email(self):

        data = {
            'email': 'foobar3@example.com' * 30,
            'name': 'foobar',
            'username': 'foobar',
            'password': 'foobarpassword',
            'address': 'street address test - 119',
            'cpf': '626.592.330-68',
            'phone_number': '48994618114'
        }

        self.response_field(data, 'email')

    def test_create_user_with_preexisting_email(self):
        data = {
            'email': 'testuser@gmail.com',
            'name': 'test4',
            'username': 'foobar',
            'password': 'foobarpassword',
            'address': 'street address test - 119',
            'cpf': '626.592.330-71',
            'phone_number': '48994618110'
        }

        self.response_field(data, 'email')

    def test_create_user_with_no_name(self):
        data = {
            'email': 'foobar4@example.com',
            'name': '',
            'username': 'foobar',
            'password': 'foobarpassword',
            'address': 'street address test - 119',
            'cpf': '626.592.330-71',
            'phone_number': '48994618112'
        }

        self.response_field(data, 'name')


    #
    # def test_create_user_with_preexisting_email(self):
    #     data = {
    #         'username': 'testuser',
    #         'email': 'test@example.com',
    #         'password': 'testuser'
    #     }
    #
    #     self.response_field(data, 'email')
    #
    # def test_create_user_with_invalid_email(self):
    #     data = {
    #         'username': 'testuser',
    #         'email': 'testing',
    #         'password': 'testuser'
    #     }
    #
    #     self.response_field(data, 'email')
    #
    # def test_create_user_with_no_email(self):
    #     data = {
    #         'username': 'testuser',
    #         'email': '',
    #         'password': 'testuser'
    #     }
    #
    #     self.response_field(data, 'email')
    #

    def response_field(self, data, field):
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.User.objects.count(), 1)
        self.assertEqual(len(response.data[field]), 1)
