from django.test import TestCase
from django.contrib.auth.models import User
from .forms import ThreadForm, MessageForm


class TestThreadForm(TestCase):
    """
    Test if create thread form is left blank when submitted
    """
    def test_username_is_required(self):
        form = ThreadForm({'username': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')


class TestMessageForm(TestCase):
    """
    Test if message thread form is left blank when submitted
    """
    def test_message_is_required(self):
        form = MessageForm({'username': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')


class TestViews(TestCase):
    def setUp(self):
        """
        Create testuser to test pages where
        you need to be logged in to view
        """
        testuser = User.objects.create_user(
            username="test_user",
            password="test_password",
            email="test@test.com"
        )
        testuser.save()

    def test_inbox_view(self):
        """
        Test if testuser can access inbox
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/inbox/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inbox.html')

    def test_create_thread_view(self):
        """
        Test if testuser can access create-thread page
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/inbox/create-thread')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_thread.html')
