from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('myapp:category_list', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE) 
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)   
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse('myapp:product_detail', args=[self.slug])