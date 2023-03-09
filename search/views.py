from django.shortcuts import render
from django.views import View
from django.db.models import Q
from posts.models import Post
from profiles.models import Profile


class Search(View):
    """
    Get a list of profiles and posts
    containing the user's search query
    """
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')

        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query)
        )

        post_list = Post.objects.filter(
            Q(content__icontains=query)
        )

        context = {
            'profile_list': profile_list,
            'post_list': post_list,
        }

        return render(request, 'search.html', context)
