from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from .models import Product,Sale,Order

@receiver(pre_save,sender=Product)
def pre_save_slug_change(sender,instance,**kwargs):
    if "_" in instance.slug:
        instance.slug = str(instance.slug).replace("_","-").lower()
        instance.save()

"""
#auto-order
@receiver(post_save,sender=Product)
def post_save_slug_change(sender,created,instance,**kwargs):
    print('created ',created)
    if created:
        instance = Order.objects.create(author=instance.published_by)
        instance.save()
"""

#sale
@receiver(post_save,sender=Product)
def post_save_create_or_update_sale(sender,created,instance,**kwargs):
    instance = Sale.objects.get_or_create(order=instance)
    instance.price = instance.price
    instance.save()