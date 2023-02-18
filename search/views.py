from django.shortcuts import render
from django.views import View
from django.db.models import Q
from posts.models import Post


class Search(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')

        profile_list = Profile.objects.filter(
            Q(user__username__icontains=query)
        )

        post_list = Post.objects.filter(
            Q(post__content__icontains=query)
        )

        context = {
            'profile-list': profile_list,
            'post_list': post_list,
        }

        return render(request, 'search.html', context)
