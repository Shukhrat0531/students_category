from django.shortcuts import render
from .models import*
# Create your views here.

def index(request):
    category= Category.objects.all()
    return render(request, 'index.html',{'category':category})

def category_describe(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'category_describe.html',{'product':product})    