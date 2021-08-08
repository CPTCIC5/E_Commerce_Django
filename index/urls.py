from django.urls import path
from . import views

app_name='index'

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/',views.cart,name='cart'),
    path('detail/<str:slug>/',views.detail,name='detail'),
    path('order/',views.order,name='order'),
    path('search/',views.search,name='search'),
    path('seller',views.seller,name='seller')
]