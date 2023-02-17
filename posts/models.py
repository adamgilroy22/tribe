from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    posted_on = models.DateTimeField(default=timezone.now)
    is_flagged = models.BooleanField(default=False, editable=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        """
        String representation
        """
        return self.content
