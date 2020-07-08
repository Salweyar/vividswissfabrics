from django.db import models

# Create your models here.
class newCollection(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(decimal_places=2, max_digits=9999)
    