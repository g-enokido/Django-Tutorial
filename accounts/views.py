from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
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
        return render(request, 'accounts/create_blog.html', {'form': form})


# Create your views here.


@login_required
def ShowsUserPage(request, pk):
    blogs = Blog.objects.filter(author_id=pk)
    blogs_deal = blogs.count()
    return render(request, 'accounts/user_page.html', {'blog': blogs, 'blogs_deal': blogs_deal})


@login_required
def ChangeUserData(request, pk):
    if request.method == "POST":
        user = get_object_or_404(CustomUser, id=pk)
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        form.password = user.password

        if form.is_valid():
            change_data = form.save(commit=False)
            change_data.save()
            return redirect('show_user', pk=user.pk)
        else:
            return render(request, 'accounts/user_customize.html', {'form': form, 'user': user})

    else:
        user = get_object_or_404(CustomUser, id=pk)
        form = CustomUserChangeForm()
        return render(request, 'accounts/user_customize.html', {'form': form, 'user': user})


def GetUserData(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    return render(request, 'accounts/show_data.html', {'userdata': user})


@login_required
def Delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('user_page', pk=request.user.id)
