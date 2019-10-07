from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils import timezone
from .forms import BlogForm
from django.shortcuts import render, redirect


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


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
