from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """test if the email is normalized"""
        email = 'test@RGHU.COM'
        user = get_user_model().objects.create_user(email, '123werd')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_validated(self):
        """Test new user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')


    def test_create_new_super_user(self):
        """Test super user has create function working"""
        user = get_user_model().objects.create_super_user(
            'jddbf@jbfn.com',
            'pass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
