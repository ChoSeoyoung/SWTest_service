from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
from .forms import QuestionForm, AnswerForm
from django.utils import timezone

# Create your views here.
def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return render(request,'questions/questions.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question }
    return render(request,'questions/question.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        question = form.save(commit=False)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('questions:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'questions/createQuestion.html', context)

def update(request,question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('questions:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'question': question}

    return render(request, 'questions/updateQuestion.html', context)

def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('questions:index')

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('questions:detail', question_id = question.id)
    else:
        form = AnswerForm()
        context = {'form': form, 'question': question}
        return render(request, 'questions/exams.html', context)

