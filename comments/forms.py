from django import forms
from .models import Comment


class CommentForm (forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Leave Your Reply...'
        }))

    class Meta:
        model = Comment
        fields = ['comment']
