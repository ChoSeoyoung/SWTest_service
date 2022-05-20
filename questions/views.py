from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request,'questions/questions.html',context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question' : question }
    return render(request,'questions/question.html', context)

def modify(request,question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request,'questions/editQuestion.html', context)

def delete(request):
    return HttpResponse("질문 삭제")
