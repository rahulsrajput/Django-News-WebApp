from django.contrib import admin
from .models import Category,Article
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','category','user']
    prepopulated_fields = {"slug": ('title',)}