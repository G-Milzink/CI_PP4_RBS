# Third party imports:
from django.urls import path
# Internal imports:
from contact import views


# Url's for the contact page
urlpatterns = [
    path('contact/', views.ContactMessage.as_view(), name='contact'),
]
