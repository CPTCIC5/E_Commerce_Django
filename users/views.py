from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        print(password1)
        if password1==password2:
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                print('Already taken')
            new_user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
            new_user.save()
            return HttpResponseRedirect('/')
    return render(request,'users/register.html')


@login_required
def order_history(request):
    history=User.objects.all()
    return render(request,'users/order_history.html',{'history':history})