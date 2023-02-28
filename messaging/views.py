from django.shortcuts import render
from django.views import View
from django.db.models import Q
from .models import MessageThread, MessageModel


class MessageThreads(View):
    """
    View message threads
    """
    def get(self, request, *args, **kwargs):
        threads = MessageThread.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads,
        }

        return render(request, 'inbox.html', context)
