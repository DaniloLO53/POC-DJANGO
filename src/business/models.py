from django.db import models
from django.utils import timezone

import datetime


class Thumbnail(models.Model):
    content = models.CharField(max_length=200)
    updated_at = models.DateTimeField("date updated")
    created_at = models.DateTimeField("date created")


class Seller(models.Model):
    sellername = models.CharField(max_length=100)
    email = models.CharField(max_length=75, default="noemail@noemail.com")
    password = models.CharField(max_length=32, default="1234")
    updated_at = models.DateTimeField("date updated")
    created_at = models.DateTimeField("date created")


class Product(models.Model):
    thumbnail = models.ForeignKey(Thumbnail, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=11, decimal_places=2)
    stock = models.IntegerField(default=1)
    updated_at = models.DateTimeField("date updated")
    created_at = models.DateTimeField("date created")


class User(models.Model):
    username = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=32)
    updated_at = models.DateTimeField("date updated")
    created_at = models.DateTimeField("date created")


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sellername = models.CharField(max_length=100)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=32)
    updated_at = models.DateTimeField("date updated")
    created_at = models.DateTimeField("date created")
