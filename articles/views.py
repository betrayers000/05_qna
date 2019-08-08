from django.shortcuts import render, redirect
from .models import Question
import requests

# Create your views here.
def new(request):
    return render(request, 'new.html')


def create(request):
    #get request info
    user = request.GET.get('user')
    title = request.GET.get('title')
    content = request.GET.get('content')

    #create db
    question = Question(title=title, content=content, user=user)    
    question.save()
    return redirect('/questions/') 


def index(request):
    questions = Question.objects.all()
    res = requests.get('http://www.naver.com')
    context = {
        'questions': questions,
        'res': res,
    }
    return render(request, 'index.html', context)