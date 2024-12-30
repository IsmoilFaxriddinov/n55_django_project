from django.shortcuts import render

from blogs.models import BlogModel

def blog_page_view(request):
    blogs = BlogModel.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blog_list.html', context)
