from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Product,Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q

def home(request):
    n1=Product.objects.all()
    return render(request,'index/home.html',{'n1':n1})

def cart(request):
    return render(request,'index/cart.html')

def detail(request,slug):
    n2=Product.objects.filter(slug=slug)
    return render(request,'index/detail.html',{'n2':n2})

def search(request):
    if request.method=='POST':
        searched=request.POST.get('searched')
        print(searched)
        x1=Product.objects.filter(Q(title__startswith=searched) | Q(title__icontains=searched))
        if len(searched)>200:
            x3="UR TEXT IS TOO LONG"
            return render(request,'index/search.html',{'x3':x3,'searched':searched})
        return render(request,'index/search.html',{'x1':x1,'searched':searched})
    #return render(request,'index/search.html',{'searched':searched,'x1':x1})
    return HttpResponseRedirect(reverse('index:home'))

@login_required
def order(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        author=request.user
        phone_no=request.POST.get('phone_no')
        address=request.POST.get('address')
        zipcode=request.POST.get('zipcode')

        entry1=Order(name=name,email=email,author=author,phone_no=phone_no,address=address,zipcode=zipcode)
        entry1.save()
        messages.success(request,'ORDERED!')
        #return HttpResponseRedirect('/')
        return HttpResponseRedirect(reverse('index:home'))
    return render(request,'index/order.html')

@login_required
def seller(request):
    if request.method=='POST':
        title=request.POST.get('title')
        price=request.POST.get('price')
        pic=request.POST.get('pic')
        published_by=request.user
        desc=request.POST.get('desc')
        slug=request.POST.get('slug')
        if Product.objects.filter(title=title).exists():
            return messages.warning(request,'TITLE ALREADY EXISTS')
        if Product.objects.filter(slug=slug).exists():
            return messages.warning(request,'ENDPOINT ALREADY TAKEN')
        added=Product(title=title,price=price,pic=pic,published_by=published_by,desc=desc,slug=slug)
        added.save()
        messages.success(request,'Product added')
        return HttpResponseRedirect(reverse('index:home'))
    return render(request,'index/sell_product.html')