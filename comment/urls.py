from django.urls import path
from . import views

urlpatterns = [
    path('submission/', views.Comment, name='comment_submmit')
]
