from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):
    def test_post_content_is_required(self):
        form = PostForm({'content': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')
