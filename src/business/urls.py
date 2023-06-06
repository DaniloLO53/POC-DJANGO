from django.urls import path

from . import views

app_name = "business"
urlpatterns = [
    path("sign-up/", views.signup, name="sign-up"),
    path("sign-in/", views.signin, name="sign-in"),
    path("index/", views.index, name="index"),
]
