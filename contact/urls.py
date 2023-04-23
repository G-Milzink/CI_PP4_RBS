from django.urls import path
from contact import views


urlpatterns = [
    path('contact/', views.ContactMessage.as_view(), name='contact'),
]
