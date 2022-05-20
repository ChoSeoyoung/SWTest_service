from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('question/', views.detail),
    path('modify/', views.modify),
    path('delete/', views.delete),
]