from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Create form object for Post model
    """

    class Meta:
        model = Post
        fields = ['content']
