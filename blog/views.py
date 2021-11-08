from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def allblogs(request):
    blog = Blog.objects
    return render(request, "blog/allblogs.html", {"blog":blog})

def expand(request, blog_id):
    detailedblog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': detailedblog})