from django.shortcuts import render
from .models import *

# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def categories(request):
    return {
        'categories': Category.objects.all()
    }