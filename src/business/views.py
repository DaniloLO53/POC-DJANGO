from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import User


def index(request):
    users = User.objects.order_by('created_at')[:5]
    context = {
        "users": users,
    }
    return render(request, "business/index.html", context)


def about(request):
    return HttpResponse('Hey, this is the about page!')


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "business/detail.html", {"user": user})
