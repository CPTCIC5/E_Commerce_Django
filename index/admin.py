from django.contrib import admin
from .models import Product,Order

admin.site.site_header='ECOMMERCE'
admin.site.site_title='MANAGEMENT LOGIN'
admin.site.index_title='WELCOME ADMIN'

admin.site.register(Product)
admin.site.register(Order)
