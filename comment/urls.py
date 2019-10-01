from django.urls import path
from . import views

urlpatterns = [
    path('submission/', views.Comment)
]
