from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from polls import apiviews


# Create your tests here.
class TestPoll(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

        self.client = APIClient()

        self.user1 = self.setup_user('test_user1', 'test_user1@test.com', 'test_user1')
        self.token = Token.objects.create(user=self.user1)
        self.token.save()

    @staticmethod
    def setup_user(username, email, password):
        User = get_user_model()
        return User.objects.create_user(
            username,
            email=email,
            password=password)

    # GET test with APIRquestFactory. This should return 200 for
    # success from listing polls.
    def test_list(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user1
        # try to access PollList view, /polls/
        response = self.view(request)
        self.assertEqual(
            response.status_code,
            200,
            'Expected Response Code 200, received {0} instead.'
            .format(response.status_code))

    # GET test with APIClient. This should return 200 for
    # success from listing polls.
    def test_list2(self):
        self.client.login(username='test_user1', password='test_user1')
        # try to get data from /polls/
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            'Expected Response Code 200, received {0} instead.'
            .format(response.status_code))

    # POST test with APIClient. This should return 201 for
    # success from creating a poll.
    def test_create(self):
        self.client.login(username='test_user1', password='test_user1')
        User = get_user_model()
        params = {
            "question": "How are you?",
            "created_by": User.objects.get(username='test_user1').pk
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            'Expected Response Code 201, received {0} instead.'
            .format(response.status_code))


class TestChoice(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

        self.user1 = self.setup_user('test_user1', 'test_user1@test.com', 'test_user1')
        self.token = Token.objects.create(user=self.user1)
        self.token.save()

        self.user2 = self.setup_user('test_user2', 'test_user2@test.com', 'test_user2')
        self.token = Token.objects.create(user=self.user2)
        self.token.save()

        self.create_poll(self)

    @staticmethod
    def setup_user(username, email, password):
        User = get_user_model()
        return User.objects.create_user(
            username,
            email=email,
            password=password)

    @staticmethod
    def create_poll(self):
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.client.login(username='test_user1', password='test_user1')
        self.uri = '/polls/'
        User = get_user_model()
        params = {
            "question": "How are you?",
            "created_by": User.objects.get(username='test_user1').pk
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            'Expected Response Code 201, received {0} instead.'
            .format(response.status_code))

    # GET test with APIClient. This should return 200 for success
    # from listing choices.
    def test_list(self):
        self.client.login(username='test_user1', password='test_user1')
        self.uri = '/polls/1/choices/'
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code,
            200,
            'Expected Response Code 200, received {0} instead.'
            .format(response.status_code))

    # POST test with API Client. This should return 201 for success
    # from creating a choice model.
    def test_create(self):
        self.client.login(username='test_user1', password='test_user1')
        self.uri = '/polls/1/choices/'
        params = {
            "choice_text": "test",
            "poll": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            201,
            'Expected Response Code 201, received {0} instead.'
            .format(response.status_code))

    # POST test with API Client. This should return 403 for permission
    # denied from creating a choice model.
    def test_create_permission_denied(self):
        self.client.login(username='test_user2', password='test_user2')
        self.uri = '/polls/1/choices/'
        params = {
            "choice_test": "test",
            "poll": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code,
            403,
            'Expected Response Code 403, received {0} instead.'
            .format(response.status_code))
