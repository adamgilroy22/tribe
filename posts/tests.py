from django.test import TestCase
from django.contrib.auth.models import User
from .forms import PostForm


class TestPostForm(TestCase):
    def test_post_content_is_required(self):
        """
        Test is post form is left blank when submitted
        """
        form = PostForm({'content': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')


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

    def test_following_feed(self):
        """
        Test if testuser can access following posts feed
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feed.html')

    def test_all_post_feed(self):
        """
        Test if testuser can access all posts feed
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/feed/all-posts')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_post_feed.html')
