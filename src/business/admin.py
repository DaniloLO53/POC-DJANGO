from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Thumbnail, Product, Seller

admin.site.register(Thumbnail)
admin.site.register(Product)
admin.site.register(Seller)
