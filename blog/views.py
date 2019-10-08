from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from comment.models import Comment
from .models import Post, Category
from signup.models import Blog
from .forms import PostForm, CategoryForm

# Create your views here.


def index(request):
    posts = Blog.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date').reverse()

    if 'blog' in request.session:
        del request.session['blog']

    if request.user.is_authenticated:
        request.session['own_blogs'] = Blog.objects.filter(
            author_id=request.user).count()
    return render(request, 'blog/index.html', {'articles': posts})


def post_list(request, pk):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), blog_id=pk).order_by('created_date').reverse()
    blog = get_object_or_404(Blog, pk=pk)
    request.session['blog'] = blog
    category = Category.objects.filter(blog_id=blog.id)
    category.group_by = ['category_id']

    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})


def post_detail(request, pk):
    if 'blog' not in request.session:
        blog_id = get_object_or_404(Post, pk=pk).blog_id
        blog_data = get_object_or_404(Blog, pk=blog_id)
        request.session['blog'] = blog_data

    blogId = request.session['blog'].id
    post = get_object_or_404(Post, pk=pk, blog_id=blogId)
    category = get_object_or_404(Category, pk=post.category_id, blog_id=blogId)
    comment = Comment.objects.filter(article_id=pk)

    return render(request, 'blog/post_detail.html', {'post': post, 'comment': comment, 'category': category})


@login_required
@csrf_protect
def post_new(request, pk):
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            blogs = get_object_or_404(
                Blog, pk=request.session['target_blog'].id)
            post = form.save(commit=False)
            post.author = request.user
            post.blog_id = blogs.id

            if request.POST['category_name'] != '':
                new_category = CategoryForm(request.POST)
                if new_category.is_valid():
                    create = new_category.save(commit=False)
                    create.holder = request.user
                    create.category_name = request.POST['category_name']
                    create.blog_id = request.session['target_blog'].id
                    create.updated_date = timezone.now()
                    create.save()
                post.category_id = get_object_or_404(
                    Category, category_name=request.POST['category_name']).id
            else:
                post.category_id = request.POST['category_set']

            if request.POST.get("draft_flag", True):
                post.published_date = timezone.now()

            post.save()
            blogs.published_date = timezone.now()
            blogs.save()
            return redirect('post_list', pk=post.blog_id)

    else:
        categories = Category.objects.filter(blog_id=pk)
        target_blog = get_object_or_404(Blog, pk=pk)
        request.session['target_blog'] = target_blog
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form, 'categories': categories})


@login_required
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

            blogs = get_object_or_404(Blog, pk=request.POST['blog_set'])
            blogs.published_date = timezone.now()
            blogs.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form, 'detail_flag': True})


@login_required
def post_draft_list(request, pk):
    posts = Post.objects.filter(
        published_date__isnull=True, author_id=pk).order_by('created_date')

    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list', pk=request.session['blog'].id)


def post_login(request):
    return render(request, 'blog/post_login.html')
