from accounts.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import BlogForm, LoginForm
from .models import Blog, CustomUser


class CreateUser(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class Account_login(CreateView):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                return render(request, 'registration/login.html', {'form': form, })

            login(request, user)
            return redirect('/')
        return render(request, 'registration/login.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'registration/login.html', {'form': form, })


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
        return render(request, 'accounts/signup/create_blog.html', {'form': form})


# Create your views here.


@login_required
def ShowsUserPage(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    return render(request, 'accounts/user_page.html', {'blog': blogs})


@login_required
def GetUserData(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    return render(request, 'accounts/user_page.html', {'blog': blogs})
