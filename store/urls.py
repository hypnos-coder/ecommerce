from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('update-item/',views.updateitem,name='update-item'),
    path('process-order/',views.processOrder,name='process-order')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)