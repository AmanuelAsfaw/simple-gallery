from importlib.resources import path
from operator import mod
from turtle import title
import django
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey( User, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.title

class Photo(models.Model):
    title = models.CharField(max_length=200)
    non_fungible_token = models.TextField(unique=True)
    path = models.CharField(max_length=200)
    heeght = models.FloatField()
    width = models.FloatField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

