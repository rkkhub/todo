from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating new user with emai is successful"""
        email = 'test@mytodo.com'
        password = 'mypassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@MyTodo.Com'
        user = get_user_model().objects.create_user(email, "mypassword")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test user create with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "mypassword")

    def test_create_new_superuser(self):
        """Tetst creating new superuser"""
        user = get_user_model().objects.create_superuser("email@mytodo.com",
                                                         "mypassword")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
