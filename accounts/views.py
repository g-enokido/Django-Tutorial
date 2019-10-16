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
            if user.is_active:
                login(request, user)
                return redirect('user_page')
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
def ShowsUserPage(request):
    blogs = Blog.objects.filter(author_id=request.user.id)
    blogs_deal = blogs.count()
    return render(request, 'accounts/user_page.html', {'blog': blogs, 'blogs_deal': blogs_deal})


@login_required
def ChangeUserData(request):
    if request.method == "POST":
        user = get_object_or_404(CustomUser, id=request.user.id)
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        form.password = user.password

        if form.is_valid():
            change_data = form.save(commit=False)
            change_data.save()
            return redirect('show_user')
        else:
            return render(request, 'accounts/user_customize.html', {'form': form, 'user': user})

    else:
        user = get_object_or_404(CustomUser, id=request.user.id)
        form = CustomUserChangeForm(initial={
                                    'username': user.username, 'profile_icon': user.profile_icon,
                                    'self_introduction': user.self_introduction})
        return render(request, 'accounts/user_customize.html', {'form': form})


def GetUserData(request):
    user = get_object_or_404(CustomUser, id=request.user.id)
    return render(request, 'accounts/show_data.html', {'userdata': user})


@login_required
def Delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if blog. author_id == request.user.id:
        blog.delete()
    return redirect('user_page')


@login_required
def Reject_user(request, pk):
    CustomUser.objects.filter(id=pk).update(is_active=False)
    return redirect('top_page')
