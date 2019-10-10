from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils import timezone
from .forms import BlogForm
from django.shortcuts import render, redirect
from accounts.models import Blog
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup/signup.html'


def Create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            return redirect('top_page')
    else:
        form = BlogForm()
        return render(request, 'signup/create_blog.html', {'form': form})


# Create your views here.


@login_required
def ShowsUserPage(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    return render(request, 'user/user_page.html', {'blog': blogs})


@login_required
def GetUserData(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    return render(request, 'user/user_page.html', {'blog': blogs})
