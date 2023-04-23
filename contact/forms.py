from django import forms
from crispy_forms.helper import FormHelper
from .models import Contact


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message')
