from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    photo=models.URLField(blank=True, null=True)
    price = models.IntegerField()
    stock = models.IntegerField()


    def __str__(self):
        return self.name




# Create your models here.
