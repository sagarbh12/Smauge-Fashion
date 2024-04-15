# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contact_number = models.CharField(max_length=10)
    full_name = models.CharField(max_length=20)
    email_token = models.CharField(max_length=200, blank=True, null=True)
    is_verified =models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=200, blank=True, null=True)

    def _str_(self):
        return self.username
 
