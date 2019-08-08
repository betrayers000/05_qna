from django.shortcuts import render, redirect
from .models import Question, Answer
# import requests

# Create your views here.
def new(request):
    return render(request, 'new.html')


def create(request):
    # get request info
    user = request.GET.get('user')
    title = request.GET.get('title')
    content = request.GET.get('content')

    # create db
    question = Question(title=title, content=content, user=user)    
    question.save()
    return redirect('/questions/') 


def index(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    # res = requests.get('http://www.naver.com')
    context = {
        'questions': questions,
        'answers': answers,
        # 'res': res,
    }
    return render(request, 'index.html', context)

def answer_create(request, question_id):
    # get answer info
    content = request.GET.get('content')
    # get question object
    question = Question.objects.get(id=question_id) 
    # create answer db
    # question id를 넣어주는게 아니라 객체 자체를 넣어줘야한다.
    answer = Answer(content=content, question=question)
    answer.save()
    return redirect('/questions/') 