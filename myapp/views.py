from django.shortcuts import render
from myapp.models import*
from datetime import datetime
def homepage(request):
    products=Product.objects.all()
    now=datetime.now()
    return render(request,'index.html',locals())

def product_overview(request):
    products = Product.objects.all()
    now = datetime.now()
    return render(request, 'product_overview.html', {'products': products})

# Create your views here.
