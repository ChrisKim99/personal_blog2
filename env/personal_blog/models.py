from django.db import models

# Create your models here.



class track_of_mind(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    eng_desc = models.TextField()
    kor_desc = models.TextField()

class book(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to = "books_pics")
    eng_desc = models.TextField()
    kor_desc = models.TextField()