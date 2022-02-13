from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.forms import BooleanField

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255,unique=True)
    avatar = models.CharField(max_length=500)
    skills = models.CharField(max_length=500, blank=True)
    portfolio = models.CharField(max_length=500, blank=True)
    sunday = models.BooleanField(default=False)
    monday = models.BooleanField(default=False)
    tuesday = models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    availabilty = models.CharField(max_length=500, blank=True)
    payrate = models.IntegerField(default=0)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
