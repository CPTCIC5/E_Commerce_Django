from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    pic=models.ImageField(default='default.jpg',upload_to='images')
    published_by=models.ForeignKey(User,on_delete=models.CASCADE)
    desc=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=35)

    def __str__(self):
        return self.title

class Order(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_no=models.IntegerField(default=0)
    address=models.CharField(max_length=100)
    zipcode=models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Sale(models.Model):
    order = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.amount)