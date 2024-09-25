from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def product_all(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/detail.html', {'product':product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/categories.html', {'category':category, 'products':products})