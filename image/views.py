from django.urls import reverse_lazy
from django.views import generic
from .form import SingleUploadModelForm
from .models import UploadFile
# Create your views here.


class SingleUploadWithModelView(generic.CreateView):
    model = UploadFile
    form_class = SingleUploadModelForm
    template_name = 'image/upload.html'
    success_url = reverse_lazy('app:file_list')


class FilelistView(generic.ListView):
    model = UploadFile
