from datetime import datetime
import json
from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from store.models import Order, OrderItem, Product, ShippingAdress

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created= Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0, 'get_cart_items':0}
        cartItems=order['get_cart_items']
    products=Product.objects.all()
    context={'products':products,
             'cartItems':cartItems,
             'shipping':False}
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created= Order.objects.get_or_create(customer=customer, complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items

    else:
        items=[]
        order={'get_cart_total':0,
               'get_cart_items':0}
        cartItems=order['get_cart_items']
    context={'items':items,
             'order':order,
             'cartItems':cartItems,
             'shipping':False}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
            customer = request.user.customer
            order,created= Order.objects.get_or_create(customer=customer, complete=False)
            items=order.orderitem_set.all()
            cartItems=order.get_cart_items

    else:
        items=[]
        order={'get_cart_total':0,
               'get_cart_items':0}
        cartItems=order['get_cart_items']
    context={'items':items,
             'order':order,
             'cartItems':cartItems,
             'shipping':False} 
    return render(request,'store/checkout.html',context)

def updateitem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print('action:',action)
    print('productid:',productId)
    
    customer = request.user.customer
    product=Product.objects.get(id=productId)
    order,created= Order.objects.get_or_create(customer=customer, complete=False)
  
    orderItem,created= OrderItem.objects.get_or_create(order=order, product=product)

    if action=='add':
        orderItem.quantity+=1
    elif action=='remove':
        orderItem.quantity-=1
        
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('item was added',safe=False)

def processOrder(request):
    #print('data:',request.body)
    transaction_id=datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created= Order.objects.get_or_create(customer=customer, complete=False)
        total=float(data['form']['total'])
        order.transaction_id=transaction_id
        if total==order.get_cart_total:
            order.complete=True
        order.save()
        if order.shipping==True:
            ShippingAdress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )
    return JsonResponse('Payement complete',safe=False)