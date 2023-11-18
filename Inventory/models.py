from django.db import models
from Product.models import Product

# Create your models here.
class Inventory(models.Model):
    inventory_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey("Product.Product", on_delete=models.DO_NOTHING)
    quantity_available = models.IntegerField(default=0)
    #shop_id =
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

class Sales(models.Model):
    sale_id = models.BigAutoField(primary_key=True)
    #shop_id =
    product = models.ForeignKey("Product.Product", on_delete=models.DO_NOTHING)
    quantity_sold = models.IntegerField()
    sale_date = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
    purchase = models.BigAutoField(primary_key=True)
    #shop_id =
    product = models.ForeignKey("Product.Product", on_delete=models.DO_NOTHING)
    quantity_purchased = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now=True)

class Return(models.Model):
    #product_id
    #order_id
    #date
    #reason
    pass