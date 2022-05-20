from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("질문 목록")

def detail(request):
    return HttpResponse("질문 상세")

def modify(request):
    return HttpResponse("질문 수정")

def delete(request):
    return HttpResponse("질문 삭제")
