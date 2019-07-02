from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# class UserProfileManager(BaseUserManager):
#
#     def create_user(self, email, name, password=None):
#         if not email:
#             raise ValueError('User must have an email address')
#
#         email= self.normalize_email(email)
#         user = self.model(email=email, name=name)
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, email, name, password):
#
#         user= self.create_user(email, name, password)
#
#         user.is_superuser =True
#         user.is_staff= True
#         user.save(using= self._db)
#
#         return user
#
#
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#
#     email= models.EmailField(max_length=225, unique=True)
#     name= models.CharField(max_length=225, unique=True)
#     is_active= models.BooleanField(default=True)
#     is_staff= models.BooleanField(default=False)
#
#     objects= UserProfileManager()
#
#     USERNAME_FIELD = 'name'
#     REQUIRED_FIELDS= ['name']
#
#     def get_full_name(self):
#
#         return self.name
#
#
#
#     def __str__(self):
#
#         return self.email
#


class Brand (models.Model):
    brand_name = models.CharField(max_length=255)
    is_featured = models.BooleanField()


    class Meta:
        verbose_name_plural = "brands"

    def __str__(self):
        return self.brand_name


class ProductManager(models.Manager):
    def create_product(self, name, description, price, product_image):
        if not name:
            raise ValueError('Product must have a name')


        product = self.model(name=name, description=description, price=price, product_image=product_image)


        product.save(using=self._db)

        return product


class Product (models.Model):
     name = models.CharField(max_length=255)
     description=models.TextField(max_length=2000)
     price=models.DecimalField(max_digits=10, decimal_places=2)
     is_available = models.BooleanField(default=True)
     product_image = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")
     brand= models.ManyToManyField(Brand)

     REQUIRED_FIELDS= ['name']
     objects= ProductManager()
    #  model_pic= models.ImageField(upload_to=upload_image, default='blog/images/already.png')
    #
    #
    #
    # def upload_image(self, filename):
    #     return 'post/{}/{}'.format(self.name, filename)

     def __str__(self):
        return self.name


class ShopPage (models.Model):
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)

    product = models.OneToOneField(Product,on_delete=models.CASCADE)
    instructions = models.TextField(max_length=3000)
    ingredients = models.TextField(max_length=3000)

    REQUIRED_FIELDS= ['product']


    def __str__(self):
        return self.product.name


class Gallery (models.Model):
    gallery_title= models.CharField(max_length=255, null = True)
    class Meta:
        verbose_name_plural = "galleries"
    def __str__(self):
        return self.gallery_title



class Picture (models.Model):
    title = models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    picture_upload= models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class AboutUs (models.Model):
    about = models.TextField(max_length=2000)
    get_to_know_us = models.TextField(max_length=3000)

    def __unicode__(self):
	    return 'About us'


class CartManager(models.Manager):
    def create_cart(self, total_price, number_of_products):
        if not name:
            raise ValueError('Product must have a name')


        product = self.model(name=name, description=description, price=price, product_image=product_image)


        product.save(using=self._db)

        return product


class Cart (models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_products = models.IntegerField()
    #products = models.ArrayField(model_form_class= Product)
    products = models.ManyToManyField(Product)
    objects= CartManager()


class ContactUs (models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    how_can_i_help = models.TextField(max_length=3000)
    working_hours = models.TextField(max_length=3000)

    def __unicode__(self):
	    return 'Contact us'


class LatestOffer (models.Model):
    products = models.ManyToManyField(Product)


class family (models.Model):
    brands= models.OneToOneField(Brand, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "families"


class Store (models.Model):
    store_area = models.CharField(max_length=255)
    store_city = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = "stores"


class Category (models.Model):
    category_name = models.CharField(max_length=255)
    brands = models.ManyToManyField(Brand)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name
