# Third party imports:
from django import forms
# Internal imports:
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    form for blogpost comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
