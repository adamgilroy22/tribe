from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post
from .forms import PostForm
from comments.models import Comment
from comments.forms import CommentForm
from notifications.models import Notification


class FollowingPostListView(LoginRequiredMixin, View):
    """
    Display posts on feed from people user is
    following and sort by time posted
    and create new posts using post form
    """
    def get(self, request, *args, **kwargs):
        current_user = request.user

        following_posts = Post.objects.filter(
            author__profile__followers__in=[current_user.id]
        ).order_by('-posted_on')

        paginator = Paginator(following_posts, 10)
        page_num = request.GET.get('page')
        posts = paginator.get_page(page_num)

        context = {
            'following_post_list': posts,
            'form': PostForm(),
        }

        return render(request, 'feed.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm(request.POST)

        context = {
            'post_list': posts,
            'form': form,
        }

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your post has been sent')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.add_message(
                request, messages.ERROR,
                'Oops something has went wrong, please try again!')

        return render(request.META['HTTP_REFERER'], context)


class AllPostListView(LoginRequiredMixin, View):
    """
    Display all site posts on feed sorted by time posted
    and create new posts using post form
    """
    def get(self, request, *args, **kwargs):

        all_posts = Post.objects.all().order_by('-posted_on')

        paginator = Paginator(all_posts, 10)
        page_num = request.GET.get('page')
        posts = paginator.get_page(page_num)

        context = {
            'all_post_list': posts,
            'form': PostForm(),
        }

        return render(request, 'all_post_feed.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')
        form = PostForm(request.POST)

        context = {
            'post_list': posts,
            'form': form,
        }

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your post has been sent')
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.add_message(
                request, messages.ERROR,
                'Oops something has went wrong, please try again!')

        return render(request.META['HTTP_REFERER'], context)


class PostDetailView(LoginRequiredMixin, View):
    """
    View individual posts in more detail
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        all_comments = Comment.objects.filter(post=post).order_by('-posted_on')

        paginator = Paginator(all_comments, 5)
        page_num = request.GET.get('page')
        comments = paginator.get_page(page_num)

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        if request.method == "POST":
            form = CommentForm(request.POST)

            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.author = request.user
                new_comment.post = post
                new_comment.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Your comment has been submitted')
                notification = Notification.objects.create(
                    notification_type=2, from_user=request.user, to_user=post.author, post=post)
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.add_message(
                    request, messages.ERROR,
                    'Oops something has went wrong, please try again!')

        comments = Comment.objects.filter(post=post).order_by('-posted_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete posts
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('feed')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete comments
    """
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit comments
    """
    model = Comment
    fields = ['comment']
    template_name = 'comment_edit.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class LikePost(LoginRequiredMixin, View):
    """
    Like and unlike posts
    """
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_liked = False

        for like in post.likes.all():
            if like == request.user:
                is_liked = True

        if not is_liked:
            post.likes.add(request.user)
            notification = Notification.objects.create(notification_type=1, from_user=request.user, to_user=post.author, post=post)

        if is_liked:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
