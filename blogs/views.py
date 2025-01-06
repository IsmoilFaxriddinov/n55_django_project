from django.db.models import Count
from django.shortcuts import render

from blogs.models import BlogModel
from pages.forms import BlogDetailForm

def blog_page_view(request):
    blogs = BlogModel.objects.all()
    most_liked_blogs = BlogModel.objects.all().order_by('likes')[:3]
    last_blogs = BlogModel.objects.order_by('-created_at')[:4]
    context = {
        'blogs': blogs,
        'most_liked_blogs': most_liked_blogs,
        'last_blogs': last_blogs 
    }
    return render(request, 'blogs/blog_list.html', context)

def blog_detail_view(request, pk):
    blog = BlogModel.objects.filter(id=pk).first()
    if blog is not None:
        context = {
            'blog': blog
        }
        return render(request, 'blogs/blog_detail.html', context)
    elif request.method == "GET":
        return render(request, 'blogs:blog_detail.html')
    elif request.method == "POST":
        form = BlogDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blogs:blog_detail.html')
        else:
            context = {
                'errors': form.errors
            }
            return render(request, 'blogs:blog_detail.html')
    else:
        return render(request, 'pages/404.html')
    

