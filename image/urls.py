from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('upload/', views.SingleUploadWithModelView.as_view(), name='uploader'),
    path('upload/list', views.FilelistView, name='file_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
