from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField  
# Import slugify to generate slugs from strings
from django.utils.text import slugify 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = HTMLField()
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(default='', max_length=100, unique=True)
    image = models.ImageField(null=True , blank=True, upload_to='02_news_site/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)