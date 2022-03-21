from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Task

from todo.serializers import TaskSerializer

TASKS_URL = reverse('todo:task-list')


def detail_url(args):
    return reverse('todo:task-list', args)


def sample_task(user, **kwargs):
    default = {
        'title': 'test task-1',
    }
    default.update(kwargs)
    return Task.objects.create(user=user, **default)


class PublicTodoTests(TestCase):
    """Tests for all todo api methods"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Tests that authentication is required for listing tasks"""
        res = self.client.get(TASKS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTodoTests(TestCase):
    """Tests for all todo api methods"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="api_test_user@mytodo.com",
            password="mypassword"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_tasks_api(self):
        """Tests that authenticated user is able to list all tasks"""
        for n in range(5):
            Task.objects.create(user=self.user, title=f"Task{n}")

        res = self.client.get(TASKS_URL)

        tasks = Task.objects.all().order_by('-title')
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_limited_to_user(self):
        """Test that the tasks are returned only for the authenticated user"""
        user2 = get_user_model().objects.create_user(
            email="unauth_test_user@mytodo.com",
            password="testpassword")
        Task.objects.create(
            user=user2, title="My test task for other user")
        Task.objects.create(
            user=self.user, title="My test task for auth user")

        res = self.client.get(TASKS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_create_task_api(self):
        """Test that authenticated user is able to create new task"""
        payload = {'title': 'Create task', }
        res = self.client.post(TASKS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(payload['title'], res.data['title'])
