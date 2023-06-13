from django.contrib import admin
from RestAPP.models import Products
# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'pname', 'category', 'price', 'supplier', 'supplierid']
