from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from rest_framework import generics


class Brand (models.Model):
    brand_name = models.CharField(max_length=255)
    is_featured = models.BooleanField()
    class Meta:
        verbose_name_plural = "brands"

    def __str__(self):
        return self.brand_name


class Category (models.Model):
    category_name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Family (models.Model):
    family_name= models.CharField(max_length=255, null =True)
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)
    is_featured= models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "families"


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
     in_stock = models.BooleanField(default=False)
     product_image = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")
     family= models.ForeignKey(Family, on_delete=models.CASCADE, null=True)
     instructions = models.TextField(max_length=3000, null=True)
     ingredients = models.TextField(max_length=3000, null=True)
     latest= models.BooleanField(default=False)
     best_seller= models.BooleanField(default=False)
     category= models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
     short_line_1=models.CharField(max_length=255, null=True)
     short_line_2= models.CharField(max_length=255, null=True)
     short_line_3= models.CharField(max_length=255, null=True)
     #cart= models.ForeignKey(Cart, on_delete=models.CASCADE)
     REQUIRED_FIELDS= ['name']
     objects= ProductManager()
    #  model_pic= models.ImageField(upload_to=upload_image, default='blog/images/already.png')
    # def upload_image(self, filename):
    #     return 'post/{}/{}'.format(self.name, filename)

     def __str__(self):
        return self.name




class Picture (models.Model):
    title = models.CharField(max_length=255)
    subtitle=models.TextField(max_length=3000)
    picture_upload= models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")
    action_button= models.TextField(max_length=3000, null=True)



    def __str__(self):
        return self.title


class AboutUs (models.Model):
    about = models.TextField(max_length=2000)
    get_to_know_us = models.TextField(max_length=3000)

    def __unicode__(self):
	    return 'About us'
    class Meta:
        verbose_name_plural = "About us"


class CartManager(models.Manager):
    def create_cart(self, total_price, number_of_products):


        cart = self.model(total_price=total_price, number_of_products=number_of_products)


        cart.save(using=self._db)

        return cart


class Cart (models.Model):

    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    number_of_products=models.IntegerField(default=0, null=True)
    #products = models.ArrayField(model_form_class= Product)
    products = models.ManyToManyField(Product, null=True)
    objects= CartManager()

    # def count_products(self):
    #     count = self.products.count()
    #     self.number_of_products = count
    #     self.save()
    #
    # def add_to_cart(self, product_id):
    #     product = Product.objects.get(pk=product_id)
    #     try:
    #         preexisting_order = CartItem.objects.get(product=product, cart=self)
    #         preexisting_order.quantity += 1
    #         preexisting_order.save()
    #     except CartItem.DoesNotExist:
    #         new_order = CartItem.objects.create(
    #             product=product,
    #             cart=self,
    #             quantity=1
    #             )
    #         new_order.save()


    def __unicode__(self):
        return "%s" % (self.product_id)



class CartItem (models.Model):

    cart= models.ForeignKey(Cart, on_delete= models.CASCADE,null=True, blank=True)
    product= models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity= models.IntegerField(default=1)



class ContactUs (models.Model):
    client_name = models.CharField(max_length=255)
    client_email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    how_can_i_help = models.TextField(max_length=3000)

    def __unicode__(self):
	    return 'Contact us'
    class Meta:
        verbose_name_plural = "Contact us"




class LatestOffer (models.Model):
    offer_link= models.TextField(max_length=3000, null= True)
    offer_width= models.FloatField( choices=((0.33333333,'one third of the place under latest offer'),
    (0.5, 'half the place under latest offers'),(0.66666667,'2 thirds the place under latest offers'),
    (1,'the whole place under latest offers')), null=True)
    offer_image= models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%D")
    image_text= models.TextField(max_length=2000, null=True)


class Store (models.Model):
    store_area = models.CharField(max_length=255)
    store_city = models.CharField(max_length=255, null=True)
    location_longitude = models.CharField(max_length=255, null=True)
    location_latitude = models.CharField(max_length=255, null=True)
    class Meta:
        verbose_name_plural = "stores"



class Order (models.Model):
    client_number= models.CharField(max_length=255, null = True, blank=True)
    client_address= models.TextField(max_length=2000)
    client_email=models.CharField(max_length=255)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE, null =True)
    order_date= models.DateTimeField()
    # is_deliverd = models.BooleanField(default=False)
    # is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=24, default='New Order', choices=(('New Order', 'New Order'),
    ('Out for Delivery', 'Out for Delivery'),('Delivered', 'Delivered'),('Canceled', 'Canceled'),))
    quantity = models.IntegerField(default=1)
    cart_item_price =  models.IntegerField(default=0)

    def products(self):
       return CartItem.objects.filter(order=self)

    def total(self):
        return self.cart_item.product.price * self.quantity
