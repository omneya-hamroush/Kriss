from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class ProductManager(models.Manager):
    def create_product(self, name, description, price):
        if not name:
            raise ValueError('Product must have a name')


        product = self.model(name=email, description=description, price=price)


        product.save(using=self._db)

        return product



class Product (models.Model):
     name = models.CharField(max_length=255)
     description=models.TextField(max_length=2000)
     price=models.DecimalField(max_digits=10, decimal_places=2)
     is_available = models.BooleanField()

     REQUIRED_FIELDS= ['name']
     objects= ProductManager()


     def __str__(self):
        return self.name



class ShopPage (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    instructions = models.TextField(max_length=3000)
    ingredients = models.TextField(max_length=3000)

    REQUIRED_FIELDS= ['product']


    def __str__(self):
        return self.product



class Gallerie (models.Model):
    pass


class Picture (models.Model):
    title = models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    gallerie = models.ForeignKey(Gallerie, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



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


    def __str__(self):
        return self.brand_name



class Categorie (models.Model):
    category_name = models.CharField(max_length=255)
    brands = models.ManyToManyField(Brand)


    def __str__(self):
        return self.category_name
