from django.db.models import Count
from django.shortcuts import redirect, render
from blogs.forms import BlogCommentModelForm, BlogDetailForm
from blogs.models import BlogModel

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
        if request.method == "GET":
            context = {
                'blog': blog
            }
            return render(request, 'blogs/blog_detail.html', context)
        elif request.method == "POST":
            form = BlogDetailForm(request.POST)
            if form.is_valid():
                form.save()
                context = {
                    'blog': blog,
                    'message': 'yuborildi 👍'
                }
                return render(request, 'blogs/blog_detail.html', context)
            else:
                context = {
                    'blog': blog,
                    'errors': form.errors
                }
                return render(request, 'blogs/blog_detail.html', context)
    else:
        return render(request, 'pages/404.html')

def blog_comment_view(request, blog_id):
    if request.method == "POST":
        try:
            blog = BlogModel.objects.get(id=blog_id)
        except BlogModel.DoesNotExist:
            return render(request, 'pages/404.html')
        
        form = BlogCommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect('next')
            