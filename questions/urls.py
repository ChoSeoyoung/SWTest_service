from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('question/<int:question_id>', views.detail),
    path('modify/<int:question_id>', views.modify),
    path('question/delete/', views.delete),
]