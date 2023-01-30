from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)


    def __str__(self):
        return self.title