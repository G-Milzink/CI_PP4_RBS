# Third party imports:
from django import forms
from crispy_forms.helper import FormHelper
# Internal imports:
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    form allowing the user to send a message to restaurant.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message')
