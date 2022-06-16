from django.contrib import admin

from store.models import Customer, Order, OrderItem, Product, ShippingAdress

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)



# Register your models here.
