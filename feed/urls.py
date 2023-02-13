from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='feed'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
]
