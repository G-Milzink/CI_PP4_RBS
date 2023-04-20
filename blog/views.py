from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from .models import Blogpost
from .forms import CommentForm


class PostList(generic.ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4

    def get(self, request, *args, **kwargs):

        posts = Blogpost.objects.all()
        paginator = Paginator(Blogpost.objects.all(), 4)
        page = request.GET.get('page')
        post_list = paginator.get_page(page)

        return render(
            request, 'blog.html',  {'posts': posts, 'post_list': post_list})


class PostDetail(View):

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
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
