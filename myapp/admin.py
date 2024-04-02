from django.contrib import admin
from myapp.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','description','price','stock') #管理欄位
admin.site.register(Product, ProductAdmin)
# Register your models here.
