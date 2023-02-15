from django.urls import path
from .views import ProfileView, ProfileEditView

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
]
