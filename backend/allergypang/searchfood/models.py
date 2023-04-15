from django.db import models

# 하나의 식품엔 다양한 성분, 성분은 여러 식품에 포함 가능

class FoodModel(models.Model): #식품명
    barcode = models.TextField(max_length=13)
    #materials = models.ManyToManyField(Material)


class Material(models.Model): #원재료 
    name=models.CharField(max_length=50)
