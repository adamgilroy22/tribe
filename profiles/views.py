from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Profile
from posts.models import Post
from posts.forms import PostForm
from notifications.models import Notification


class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        user = profile.user
        user_posts = Post.objects.filter(author=user).order_by('-posted_on')

        paginator = Paginator(user_posts, 10)
        page_num = request.GET.get('page')
        posts = paginator.get_page(page_num)

        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        follower_count = len(followers)

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'follower_count': follower_count,
            'is_following': is_following,
            'form': PostForm(),
        }

        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)

        context = {
            'form': form,
        }

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect(request.META['HTTP_REFERER'])

        return render(request.META['HTTP_REFERER'], context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'bio', 'profile_pic', 'bg_pic']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.add(request.user)

        notification = Notification.objects.create(notification_type=3, from_user=request.user, to_user=profile.user)

        return redirect('profile', pk=profile.pk)


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)


class FollowersList(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk)
        followers = profile.followers.all()

        context = {
            'profile': profile,
            'followers': followers,
        }

        return render(request, 'followers_list.html', context)
