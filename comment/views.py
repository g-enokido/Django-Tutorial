from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect
from .forms import CommentForm


@csrf_protect
def Comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            elif request.POST["author"] is None:
                post.author = '名無しさん'
            else:
                post.author = form["author"].value()
            post.article_id = pk
            post.save()
            return redirect('post_detail', pk=pk)
        return redirect('post_detail', pk=pk)
    else:
        return redirect('post_detail', pk=pk)


# Create your views here.
