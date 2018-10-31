from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(author=User.objects.get(username='ttala')).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})