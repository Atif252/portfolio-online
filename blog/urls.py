from django.urls import path
from blog.views import (
    list_blogs_view,
    detail_blog_view,
    delete_blog_view,
)

app_name = 'blog'

urlpatterns = [
    path('', list_blogs_view, name='blogs_list'),
    path('<slug>', detail_blog_view, name='blog_detail'),
]