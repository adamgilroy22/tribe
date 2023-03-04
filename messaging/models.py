from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MessageThread(models.Model):
    """
    Conversations between users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')


class MessageModel(models.Model):
    """
    Messages inside conversations between users
    """
    thread = models.ForeignKey(
        'MessageThread', related_name='+', on_delete=models.CASCADE,
        blank=True, null=True)
    message_sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    message_receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='+')
    message_content = models.CharField(max_length=500)
    sent_at = models.DateTimeField(default=timezone.now)
