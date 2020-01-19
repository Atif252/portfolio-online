from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost

def list_blogs_view(request):
    context = {}
    blogs = BlogPost.objects.all()
    context['blogs'] = blogs
    return render(request, 'blog/blogs.html', context)


def detail_blog_view(request, slug):
    context = {}
    blog = BlogPost.objects.get(slug=slug)
    context['blog'] = blog
    return render(request, 'blog/detail_blog.html', context)

def delete_blog_view(request, slug):
    context = {}
    try:
        blog = BlogPost.objects.get(slug=slug)
        blog.delete()
        context['response'] = 'Successfully Deleted'
    except BlogPost.DoesNotExist:
        context['response'] = 'No corresponding blog Found'
    return render(request, 'blog/delete_blog.html', context)




def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) |
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))