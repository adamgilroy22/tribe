from django.urls import path
from .views import ProfileView, ProfileEditView, AddFollower, RemoveFollower, FollowersList

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers', FollowersList.as_view(), name='followers-list'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
]
