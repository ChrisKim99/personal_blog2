from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.


# These two classes will merge together in forms.py file

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__ (self):
        return self.name
    
    def get_absolute_url(self):
        # whenever we create post, it gives you id 
        
        #return reverse('article', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length= 250)
    body = RichTextField(blank=True, null=True)

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        # whenever we create post, it gives you id 
        
        #return reverse('article', args=(str(self.id)))
        return reverse('home')