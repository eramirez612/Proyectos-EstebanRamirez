from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    stock = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
