from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    ROLES = (
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='user')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
