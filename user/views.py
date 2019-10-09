from django.shortcuts import render
from signup.models import Blog
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def ShowsUserPage(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    return render(request, 'user/user_page.html', {'blog': blogs})


@login_required
def GetUserData(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    return render(request, 'user/user_page.html', {'blog': blogs})
