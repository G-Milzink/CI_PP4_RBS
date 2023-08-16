# Third party imports:
from django.urls import path
# Internal imports:
from . import views


# Urls for the Blog (lists all posts), post-detail (shows full post)
# and post-like(handles liking posts)
urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
