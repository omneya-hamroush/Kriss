from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin




class Product (models.Model):
     name = models.CharField(max_length=255)
     description=models.TextField(max_length=2000)
     price=models.DecimalField(max_digits=10, decimal_places=2)


     REQUIRED_FIELDS= ['name']



class ShopPage (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    instructions = models.TextField(max_length=3000)
    ingredients = models.TextField(max_length=3000)

    REQUIRED_FIELDS= ['product']



class Gallerie (models.Model):
    pass


class Picture (models.Model):
    title = models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    gallerie = models.ForeignKey(Gallerie, on_delete=models.CASCADE)


class AboutU (models.Model):
    about = models.TextField(max_length=2000)
    get_to_know_us = models.TextField(max_length=3000)


class Cart (models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_products = models.IntegerField()


class ContactU (models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    how_can_i_help = models.TextField(max_length=3000)
    working_hours = models.TextField(max_length=3000)




class Store (models.Model):
    location = models.CharField(max_length=255)



class Brand (models.Model):
    brand_name = models.CharField(max_length=255)
    is_featured = models.BooleanField()


class Categorie (models.Model):
    category_name = models.CharField(max_length=255)
    brands = models.ManyToManyField(Brand)
