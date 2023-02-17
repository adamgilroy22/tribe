from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .models import Post
from .forms import PostForm
from comments.models import Comment
from comments.forms import CommentForm


class PostListView(LoginRequiredMixin, View):
    """
    Display posts on feed sorted by time posted
    and create new posts using post form
    """
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')

        context = {
            'post_list': posts,
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
            return redirect(request.META['HTTP_REFERER'])

        return render(request, 'feed.html', context)


class PostDetailView(LoginRequiredMixin, View):
    """
    View individual posts in more detail
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        comments = Comment.objects.filter(post=post).order_by('-posted_on')

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
                return redirect(request.META['HTTP_REFERER'])

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

        if is_liked:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
