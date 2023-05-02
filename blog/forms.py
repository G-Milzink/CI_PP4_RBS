from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    form for blogpost comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
