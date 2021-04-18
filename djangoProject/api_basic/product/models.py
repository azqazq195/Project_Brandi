from django.db import models


# Create your models here.

class Product(models.Model):
    # title = models.CharField(max_length=100)
    # author = models.CharField(max_length=100)
    # email = models.EmailField(max_length=100)
    # date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    image = models.CharField(max_length=120)
    lprice = models.IntegerField(max_length=50)
    hprice = models.IntegerField(max_length=50)
    mallName = models.CharField(max_length=120)
    productId = models.IntegerField(max_length=50)
    productType = models.IntegerField(max_length=50)
    brand = models.CharField(max_length=120)
    maker = models.CharField(max_length=120)
    category1 = models.CharField(max_length=120)
    category2 = models.CharField(max_length=120)
    category3 = models.CharField(max_length=120)
    category4 = models.CharField(max_length=120)

    def __str__(self):
        return self.title
