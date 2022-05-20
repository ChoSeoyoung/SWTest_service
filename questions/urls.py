from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.list, name='list'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('question/update/<int:question_id>/', views.update, name='update'),
    path('question/delete/<int:question_id>/', views.delete, name='delete'),
    path('question/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/answer/result/<int:answer_id>/', views.answer_result, name='answer_result'),
]