# The Dot Before is show that it's the same directory
from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
     posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    #{}, is a place in which we can add some things for the template to use
     return render(request,'blog/post_list.html',{'posts':posts})
     
def post_detail(request,pk):
     post = get_object_or_404(Post, pk=pk)
     return render(request, 'blog/post_detail.html',{'post':post})