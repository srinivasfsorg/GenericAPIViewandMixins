from django.db import models

# Create your models here.

class Products(models.Model):
    pid = models.IntegerField()
    pname = models.CharField(max_length=40)
    category = models.CharField(max_length=20)
    price = models.FloatField()
    supplier = models.CharField(max_length=40)
    supplierid = models.CharField(max_length=20)


    
