from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.



class track_of_mind(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    body = RichTextField(blank=True, null=True)

class book(models.Model):

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