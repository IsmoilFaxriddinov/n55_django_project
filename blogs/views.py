from django.shortcuts import render

from blogs.models import BlogModel

def blog_page_view(request):
    blogs = BlogModel.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blogs/blog_list.html', context)

def blog_detail_view(request, pk):
    blog = BlogModel.objects.filter(id=pk).first()
    if blog is not None:
        context = {
            'blog': blog.first()
        }
        return render(request, 'blogs/blog_detail.html', context)
    else:
        return render(request, 'pages/404.html')
