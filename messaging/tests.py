from django.test import TestCase
from .forms import ThreadForm, MessageForm


class TestThreadForm(TestCase):
    def test_username_is_required(self):
        form = ThreadForm({'username': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')


class TestMessageForm(TestCase):
    def test_message_is_required(self):
        form = MessageForm({'username': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')
