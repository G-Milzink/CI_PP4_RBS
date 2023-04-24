from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm


def get_user_instance(request):
    """
    if logged in, retreive user details.
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class ContactMessage(View):
    """
    display contact form and insert email when logged in
    """
    template_name = 'contact/contact.html'
    success_message = 'Your message was sent.'

    def get(self, request, *args, **kwargs):
        """
        Retrieve user email and insert into email field
        """
        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactForm(initial={'email': email})
        else:
            contact_form = ContactForm()
        return render(request, 'contact.html',
                      {'contact_form': contact_form})

    def post(self, request):
        """
        if form is valid, post to database
        """
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(
                request, "Message has been sent")
            return render(request, 'message_sent.html')

        return render(request, 'contact.html',
                      {'contact_form': contact_form})
