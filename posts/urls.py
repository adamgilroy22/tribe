from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostDeleteView, CommentDeleteView, CommentEditView, LikePost

urlpatterns = [
    path('', PostListView.as_view(), name='feed'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/edit/<int:pk>', CommentEditView.as_view(), name='comment-edit'),
    path('post/<int:pk>/like', LikePost.as_view(), name='post-like'),
]
