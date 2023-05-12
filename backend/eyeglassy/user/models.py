from product.models import Glasses
from django.contrib.auth.models import AbstractBaseUser
from product.models import  Glasses
from django.db import models

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    face_shape = models.CharField(max_length=20, null=True, blank=True)
    glasses = models.ManyToManyField(Glasses, related_name='users', blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
