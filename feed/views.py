from django.shortcuts import render
from django.views import View
from posts.models import Post
from posts.forms import PostForm
from comments.models import Comment
from comments.forms import CommentForm


class PostListView(View):
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

        return render(request, 'feed.html', context)


class PostDetailView(View):
    """
    View individual posts in more detail
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        context = {
            'post': post,
            'form': form
        }

        return render(request, 'post_detail.html', context)
