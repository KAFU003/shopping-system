from django.contrib import admin
from myapp.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=('name','description','price','order') #管理欄位
admin.site.register(Post, PostAdmin)
# Register your models here.
