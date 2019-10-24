from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.SingleUploadWithModelView.as_view(), name='uploader'),
]
