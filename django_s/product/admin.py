from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', ) # 생성된 데이터 목록을 리스트에서 name 과 price 만 미리보기가능

admin.site.register(Product, ProductAdmin)