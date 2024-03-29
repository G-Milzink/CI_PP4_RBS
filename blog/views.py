# Third party imports:
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
# Internal imports:
from .models import Blogpost
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Display a list of all blogposts
    """
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):

        posts = Blogpost.objects.all()

        return render(
            request, 'blog.html',  {'posts': posts})


class PostDetail(View):
    """
    Display a detailed view of a specific blogpost
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class PostLike(View):
    """
    Allow user to like a blogpost
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Blogpost, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
