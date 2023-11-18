from django.db import models

# Create your models here.

class OrderItems(models.Model):
    order_id = models.ForeignKey(to="OrderDetails",on_delete=models.SET_NULL)
    product_id = models.ForeignKey(to="Product",on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class OrderDetails(models.Model):
    #user_id
    total = models.IntegerField(editable=False)
    #paymentId =
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

class PaymentDetails(models.Model):
    order_id = models.ForeignKey(to="OrderItems", on_delete=models.CASCADE)
    amount = models.IntegerField(editable=False)
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)