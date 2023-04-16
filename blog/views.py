from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from .models import Blogpost


class PostList(generic.ListView):
    model = Blogpost
    queryset = Blogpost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        """
        This view renders the blog page and also all published posts
        """
        posts = Blogpost.objects.all()
        paginator = Paginator(Blogpost.objects.all(), 4)
        page = request.GET.get('page')
        post_list = paginator.get_page(page)

        return render(
            request, 'blog.html',  {'posts': posts, 'post_list': post_list})
