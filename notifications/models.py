from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Notification(models.Model):
    """
    Sends notification to user.
    notification_type: 1 = Like, 2 = Comment, 3 = Follow
    """
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(
        User,
        related_name='notification_to',
        on_delete=models.CASCADE,
        null=True)
    from_user = models.ForeignKey(
        User,
        related_name='notification_from',
        on_delete=models.CASCADE,
        null=True)
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True)
    comment = models.ForeignKey(
        'comments.Comment',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True)
    thread = models.ForeignKey(
        'messaging.MessageThread',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True)
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)
