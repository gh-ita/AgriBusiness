# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    region = models.CharField(max_length=100, blank=True, null=True)
    ethereum_address = models.CharField(max_length=42,default = "jifejoifj")
    private_key = models.CharField(max_length=66,default ="djhfvoje")
