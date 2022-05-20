from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.shortcuts import render
from .forms import QuestionForm, AnswerForm
from django.utils import timezone

# Create your views here.
def list(request):
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
            return redirect('questions:list')
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
    return redirect('questions:list')

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('questions:answer_result', answer_id=answer.id)
    else:
        form = AnswerForm()
        context = {'form': form, 'question': question }
        return render(request, 'questions/exams.html', context)

def answer_result(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question
    total = len(Answer.objects.filter(question=question))
    ans1 = int(len(Answer.objects.filter(question=question).filter(content=1))/total*100)
    ans2 = int(len(Answer.objects.filter(question=question).filter(content=2))/total*100)
    ans3 = int(len(Answer.objects.filter(question=question).filter(content=3))/total*100)
    ans4 = int(len(Answer.objects.filter(question=question).filter(content=4))/total*100)
    context = {'question': question, 'answer': answer, 'ans1': ans1, 'ans2': ans2, 'ans3': ans3, 'ans4': ans4}
    return render(request, 'questions/result.html', context)

