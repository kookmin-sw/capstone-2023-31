from django.db import models

# Create your models here.


class Glasses(models.Model):
    glasses_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True) # cost
    brand = models.CharField(max_length=20, null=True, blank=True)
    path = models.CharField(max_length=100, null=True, blank=True) # url
    image = models.ImageField(max_length=20, null=True, blank=True) # img3.jpg 같은
    shape = models.CharField(max_length=20, default='round')