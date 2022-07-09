"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    # Test models here
    def test_create_user_with_email_successful(self):
        # Test creating a user with an email is successful
        email = 'test@example.com'
        password = 'testing123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        # checked via hashing system by django
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        # test emails is normalized for new users
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.com', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'adsfusdao')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """ test that creating a user without an email raises a ValueError """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test12324')

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'adsf324'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
