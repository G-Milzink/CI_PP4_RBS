from django.db import models
from django.contrib.auth.models import User


# contact model
class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contact_user",
        null=True
    )
    name = models.CharField(
        max_length=75,
        null=True
    )
    email = models.EmailField(
        max_length=200,
        default=""
    )
    message = models.TextField()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name
