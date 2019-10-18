from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, get_object_or_404
from .forms import CommentForm
from blog.models import Post
from accounts.models import Blog


@csrf_protect
def Comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            else:
                post.author = form["author"].value()
            post.article = get_object_or_404(Post, id=pk)
            post.blog = get_object_or_404(Blog, id=post.article.blog_id)
            post.save()
            return redirect('post_detail', pk=pk)
        return redirect('post_detail', pk=pk)
    else:
        return redirect('post_detail', pk=pk)


# Create your views here.
