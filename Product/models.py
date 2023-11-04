from django.db import models
from django.conf import settings



def get_sentinel_category():
    return ProductCategory().objects.get_or_create(name="Default",parentCategory="Default")[0]

# Create your models here.
class ProductCategory(models.Model):
    #Here we going to store the product category and subcategory
    def __str__(self) -> str:
        return self.name
    choices =  (('Generic', 'Generic'), ('Specific', 'Specific'))
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15,choices=choices,blank=False,null=False,default=3)
    parentCategory = models.ForeignKey(to = "ProductCategory",on_delete=models.SET(get_sentinel_category),null=True)
