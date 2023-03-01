from django.contrib import admin
from django.urls import path
from .views import FollowingPostListView, AllPostListView, PostDetailView, PostDeleteView, CommentDeleteView, CommentEditView, LikePost, ReportPost, FlaggedPostListView

urlpatterns = [
    path('', FollowingPostListView.as_view(), name='feed'),
    path('all-posts', AllPostListView.as_view(), name='all-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/edit/<int:pk>', CommentEditView.as_view(), name='comment-edit'),
    path('post/<int:pk>/like', LikePost.as_view(), name='post-like'),
    path('post/<int:pk>/report', ReportPost.as_view(), name='post-report'),
    path('flagged-posts', FlaggedPostListView.as_view(), name='flagged-posts'),
]
