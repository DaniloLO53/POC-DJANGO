from django.urls import path

from . import views

app_name = "business"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:user_id>/", views.detail, name="detail"),
]
