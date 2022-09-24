from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    aiklama = models.TextField()
    resim = models.CharField(max_length=200)
    anasayfa = models.BooleanField(default=False)
