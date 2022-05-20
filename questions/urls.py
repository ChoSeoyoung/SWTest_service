from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('question/update/<int:question_id>/', views.update, name='update'),
    path('question/delete/<int:question_id>/', views.delete, name='delete'),
]