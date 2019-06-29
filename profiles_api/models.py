from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin




class Product (models.Model):
     name = models.CharField(max_length=255)
     description=models.TextField(max_length=2000)
     price=models.DecimalField(max_digits=10, decimal_places=2)


     REQUIRED_FIELDS= ['name']



class ShopPage (models.Model):
     product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    instructions = models.TextField(max_length=3000)
    ingredients = models.TextField(max_length=3000)



class Gallery (models.Model):
    pass


class Picture (models.Model):
    title = models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class AboutUs (models.Model):
    about = models.TextField(max_length=2000)
    get_to_know_us = models.TextField(max_length=3000)


class Cart (models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
