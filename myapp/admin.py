from django.contrib import admin
from .models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = { 'slug': ('name',) }

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'in_stock', 'author', 'price', 'created', 'updated', 'slug',] 
    list_filter = ('in_stock', 'is_active', )
    list_editable = ('price', 'in_stock', ) 
    prepopulated_fields = {'slug': ('title', )}

# @admin.site.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['all']