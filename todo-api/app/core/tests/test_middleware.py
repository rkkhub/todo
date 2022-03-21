from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from django.urls import reverse


from rest_framework import status
from rest_framework.test import APIClient


TASK_URL = reverse('todo:task-list')


def sample_get_request(client):
    return client.get(TASK_URL)


def sample_post_request(client):
    payload = {'title': 'Middleware POST test'}
    return client.post(TASK_URL, payload)


class MiddlewareResponseTests(TestCase):
    """Tests the custom middleware"""

    def setUp(self):
        self.user = get_user_model().objects.create(
            email="middlewaretest@todo.com",
            password="mypassword")
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    @override_settings(MAINTENANCE_MODE=True)
    def test_maintenance_mode_ON(self):
        """
        Tests the response for all allowed methods
        when on maintenance mode enabled
        """
        # Test GET method
        self.assertEqual(sample_get_request(self.client).status_code,
                         status.HTTP_503_SERVICE_UNAVAILABLE)

        # Test POST method
        self.assertEqual(sample_post_request(self.client).status_code,
                         status.HTTP_503_SERVICE_UNAVAILABLE)

    @override_settings(MAINTENANCE_MODE=False)
    def test_maintenance_mode_OFF(self):
        """
        Test the response for all allowed methods
        when maintenance mode disabled
        """
        # Test Get method
        self.assertEqual(sample_get_request(self.client).status_code,
                         status.HTTP_200_OK)

        # Test POST method
        self.assertEqual(sample_post_request(self.client).status_code,
                         status.HTTP_201_CREATED)
