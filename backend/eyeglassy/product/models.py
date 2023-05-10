from django.db import models

# Create your models here.


class Glasses(models.Model):
    glasses_id=models.IntegerField()
    glass_name=models.CharField(max_length=20,null=True, blank=True)