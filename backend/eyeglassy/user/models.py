from django.db import models
from product import models

class User(models.Model):
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    face_shape = models.ImageField(upload_to='user_images/')
    glasses = models.ManyToManyField('Glasses', related_name='users')


