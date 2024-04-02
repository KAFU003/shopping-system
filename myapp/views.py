from django.shortcuts import render
from myapp.models import Post
from datetime import datetime
def homepage(request):
    posts=Post.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())

# Create your views here.
