from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)


def about(request):
    return HttpResponse('Hey, this is the about page!')


def detail(request, question_id):
    return HttpResponse(f'This is the question number {question_id}')


def results(request, question_id):
    return HttpResponse(f"You're looking to results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
