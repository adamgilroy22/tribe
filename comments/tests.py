from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    def test_comment_is_required(self):
        form = CommentForm({'comment': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')
