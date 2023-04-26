from django.shortcuts import render
from django.contrib.auth.models import User


def get_user_instance(request):

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user
