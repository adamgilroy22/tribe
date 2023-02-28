from django.urls import path
from .views import MessageThreads, CreateThread

urlpatterns = [
    path('inbox/', MessageThreads.as_view(), name='inbox'),
    path('inbox/create-thread', CreateThread.as_view(), name='create-thread'),
]
