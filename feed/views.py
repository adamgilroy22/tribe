from django.shortcuts import render
from django.views import View
from posts.models import Post
from posts.forms import PostForm


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-posted_on')

        context = {
            'post_list': posts,
            'form': PostForm(),
        }

        return render(request, 'post_list.html', context)

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

        return render(request, 'post_list.html', context)
