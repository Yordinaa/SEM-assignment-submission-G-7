from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=[
            ('ADMIN', 'Admin'),
            ('USER', 'User'),
        ],
        default='USER',
    )

    def __str__(self):
        return self.username
