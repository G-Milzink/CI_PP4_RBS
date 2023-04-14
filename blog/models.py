from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Blog post model:
class Blogpost(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )
    slug = models.SlugField(
        max_length=200,
        unique=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog"
    )
    content = models.TextField()
    image = CloudinaryField(
        'image',
        default='placeholder'
    )
    expert = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User,
        related_name='blog_likes',
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


# Blog post comment model:
class Comment(models.Model):

    post = models.ForeignKey(
        Blogpost,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    approved = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} - {self.name}"
