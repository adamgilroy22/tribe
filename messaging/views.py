from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from .models import MessageThread, MessageModel
from notifications.models import Notification
from .forms import ThreadForm, MessageForm


class MessageThreads(View):
    """
    View message threads
    """

    def get(self, request, *args, **kwargs):
        threads = MessageThread.objects.filter(Q(user=request.user) | Q(receiver=request.user))  # noqa

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
            if MessageThread.objects.filter(user=request.user,
                                            receiver=receiver).exists():
                thread = MessageThread.objects.filter(
                    user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif MessageThread.objects.filter(user=receiver,
                                              receiver=request.user).exists():
                thread = MessageThread.objects.filter(
                    user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = MessageThread(
                    user=request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
        except Exception:
            messages.add_message(request, messages.ERROR,
                                 'That user does not exist')
            return redirect('create-thread')


class ThreadView(View):
    """
    View individual message thread with another user
    """

    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = MessageThread.objects.get(pk=pk)
        message_list = MessageModel.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }

        return render(request, 'thread.html', context)


class CreateMessage(View):
    """
    Create and send a message
    """

    def post(self, request, pk, *args, **kwargs):
        thread = MessageThread.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        message = MessageModel(
            thread=thread,
            message_sender=request.user,
            message_receiver=receiver,
            message_content=request.POST.get('message')
        )

        notification = Notification.objects.create(
            notification_type=4,
            from_user=request.user,
            to_user=receiver,
            thread=thread
        )

        message.save()
        return redirect('thread', pk=pk)
