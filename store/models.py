from itertools import product
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    email=models.EmailField(max_length=200, null=True)
    name=models.CharField(max_length=200, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    digital=models.BooleanField(default=False,blank=False,null=True)
    image=models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    def imageUrl(self):
        try:url=self.image.url
        except:url=''
        return url
    
class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,blank=False,null=True)
    transaction_id=models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return str(self.id)
    @property
    def shipping(self):
        shipping=False
        orderitem=self.orderitem_set.all()
        for i in orderitem:
            if i.product.digital==False:
                shipping=True
        return shipping
        
    
    @property
    def get_cart_total(self):
        orderitem=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitem])
        return total
        
    @property
    def get_cart_items(self):
        orderitem=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitem])
        return total
    
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(null=True,default=0,blank=True)
    date_aded=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def get_total(self):
        return self.product.price*self.quantity
    
class ShippingAdress(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL,null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    adress=models.CharField(max_length=200, blank=True)
    city=models.CharField(max_length=200, blank=True)
    state=models.CharField(max_length=200, blank=True)
    zip_code=models.CharField(max_length=200, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.adress


    

# Create your models here.
