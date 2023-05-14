from django.db import models

# Create your models here.


class Glasses(models.Model):
    class Meta:
        db_table = 'glasses'
    name = models.CharField(max_length=100, null=True, blank=True)
    cost = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=20, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=20, null=True, blank=True) # img3.jpg 같은
    shape = models.CharField(max_length=20, null=True, blank=True)