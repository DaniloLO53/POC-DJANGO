from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is my first django project!')


def about(request):
    return HttpResponse('Hey, this is the about page!')
