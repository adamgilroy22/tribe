from django.shortcuts import render
from .forms import PostForm


def new_post():
    """
    Create new post using form
    """
    form = PostForm()
