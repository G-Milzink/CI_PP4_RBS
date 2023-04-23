from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contact_user",
        null=True
        )
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=200,
        default=""
        )
    message = models.TextField()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name
