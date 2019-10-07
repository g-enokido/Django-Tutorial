from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from comment.models import Comment
from .models import Post
from signup.models import Blog
from .forms import PostForm

# Create your views here.


def index(request):
    posts = Blog.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/index.html', {'articles': posts})


def post_list(request, pk):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), blog_id=pk).order_by('created_date').reverse()
    blog = get_object_or_404(Blog, pk=pk)

    return render(request, 'blog/post_list.html', {'posts': posts, 'blog': blog})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(article_id=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment})


@csrf_protect
def post_new(request):
    user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blogs = get_object_or_404(Blog, pk=request.POST['blog_set'])
            post = form.save(commit=False)
            post.author = user
            post.published_date = timezone.now()
            post.blog_id = blogs.id
            post.save()

            blogs.published_date = timezone.now()
            blogs.save()
            return redirect('post_detail', pk=post.pk)

    else:
        blogs = Blog.objects.filter(author_id=user)
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form, 'blogs': blogs})


@csrf_protect
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def post_login(request):
    return render(request, 'blog/post_login.html')
