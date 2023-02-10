from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
    Create form object for Post model
    """
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Share With Your Tribe...'
        }))

    class Meta:
        model = Post
        fields = ['content']
