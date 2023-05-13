from product.models import Glasses
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    face_shape = models.CharField(max_length=20, null=True, blank=True)
    glasses = models.ManyToManyField(Glasses, related_name='users', blank=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    def __str__(self):
        return self.email
