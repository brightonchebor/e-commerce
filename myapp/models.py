from django.db import models
from django.contrib import User 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class category(models.Model):
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE) 
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)   
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField()