from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    # this deletes all data when the user is deleted
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateField()
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        # self.author is an object, so make it str
        return self.title + ' | ' + str(self.author)


class track_of_mind(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    body = RichTextField(blank=True, null=True)

class book_post(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    body = RichTextField(blank=True, null=True)

class data_structure(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    body = RichTextField(blank=True, null=True)


class data_analytic(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    body = RichTextField(blank=True, null=True)