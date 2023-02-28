from django.urls import path
from .views import MessageThreads, CreateThread

urlpatterns = [
    path('', MessageThreads.as_view(), name='inbox'),
    path('create-thread', CreateThread.as_view(), name='create-thread'),
]
