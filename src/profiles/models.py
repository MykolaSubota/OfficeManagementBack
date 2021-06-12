from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Worker(AbstractUser):
    """Модель працівника"""
    middle_name = models.CharField('По-батькові', max_length=50)
    position = models.CharField('Посада', max_length=150)
    phone = models.CharField(' Номер телефону', max_length=14)
    avatar = models.ImageField('Фото', upload_to='user/avatar/', blank=True, null=True)

class Salary(models.Model):
    """Модель зарплати працівика"""

    worker = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Працівник",
        primary_key=True
    )
    salary = models.PositiveIntegerField('Зарплата')

    class Meta:
        verbose_name = "Зарплата"
        verbose_name_plural = "Зарплати"
