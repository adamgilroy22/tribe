from django.shortcuts import render
from django.views import View
from .models import Profile
from posts.models import Post


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        posts = Post.object.filter(author=user).order_by('-posted_on')

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
        }

        return render(request, 'profile.html', context)
