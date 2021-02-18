from django.db import models
from django.contrib.auth.models import AbstractUser

class Worker(AbstractUser):
    """Модель працівника"""
    middle_name = models.CharField('По-батькові', max_length=50)
    position = models.CharField('Посада', max_length=150)
    phone = models.CharField(' Номер телефону', max_length=14)
    avatar = models.ImageField('Фото', upload_to='user/avatar/', blank=True, null=True)
