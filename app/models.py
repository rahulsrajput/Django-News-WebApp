from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(default='', blank=False, null=False, max_length=100)
    image = models.ImageField(null=True , blank=True, upload_to='02_news_site/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title