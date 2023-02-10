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
