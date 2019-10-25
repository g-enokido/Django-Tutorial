from django.views import generic
from .form import SingleUploadModelForm
from .models import UploadFile
from django.shortcuts import render, redirect
# Create your views here.


class SingleUploadWithModelView(generic.CreateView):
    def post(self, request, *arg, **kwargs):
        form = SingleUploadModelForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            form.owner = request.user
            if form.is_valid():
                image = form.save(commit=False)
                image.owner = request.user
                image.save()
                return redirect('file_list')
            else:
                return render(request, 'image/upload.html', {'form': form, })
        else:
            return redirect('login')

    def get(self, request, *args, **kwargs):
        form = SingleUploadModelForm(request.POST)
        return render(request, 'image/upload.html', {'form': form, })


def FilelistView(request):
    files = UploadFile.objects.all()
    return render(request, 'image/file_list.html', {'files': files})
