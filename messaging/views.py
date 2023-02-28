from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.contrib.auth.models import User
from .models import MessageThread, MessageModel
from .forms import ThreadForm


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


class CreateThread(View):
    """
    Create a new message thread
    """
    def get(self, request, *args, **kwargs):
        form = ThreadForm()

        context = {
            'form': form,
        }

        return render(request, 'create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        username = request.POST.get('username')

        try:
            receiver = User.objects.get(username=username)
            if MessageThread.objects.filter(user=request.user, receiver=receiver).exists():
                thread = MessageThread.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif MessageThread.objects.filter(user=receiver, receiver=user).exists():
                thread = MessageThread.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = MessageThread(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except receiver.DoesNotExist:
            return redirect('create-thread')
