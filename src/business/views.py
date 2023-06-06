from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


@login_required(login_url='/sign-in/')
def index(request):
    return render(request, "business/index.html")


def signup(request):
    if (request.method == 'POST'):
        user = User.objects.create_user(
            request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
        user.save()

        return redirect('/sign-in/')

    return render(request, "business/signup.html")


def signin(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if (user is not None):
            login(request, user)
            return redirect('/index/')

    return render(request, "business/signin.html")


def about(request):
    return HttpResponse('Hey, this is the about page!')
