from django.db import models
import datetime

class Reagent(models.Model):
    """
        Модель реагентів
    """
    name = models.CharField("Назва", max_length=150)
    characteristic = models.CharField("Характеристика", max_length=300)
    amount = models.IntegerField("Кількість", default=0)
    placing = models.CharField("Розміщення", max_length=150)
    producer = models.CharField("Виробник", max_length=100)
    valid_until = models.DateTimeField("Дійсний до")
    field_of_use = models.CharField("Галузь використання", max_length=150)
    provider = models.CharField("Постачальник", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Реагент/Матеріал"
        verbose_name_plural = "Реагентти/Матеріали"

class Device(models.Model):
    """
        Модель Прилад
    """
    YEAR_CHOICES = []

    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    name = models.CharField("Назва", max_length=150)
    producer = models.CharField("Виробник", max_length=100)
    amount = models.IntegerField("Кількість", default=0)
    placing = models.CharField("Розміщення", max_length=150)
    year_of_purchase = models.IntegerField(
        "Рік закупки",
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )
    date_of_last_inspection = models.DateField("Дата останньої перевірки")
    field_of_use = models.CharField("Галузь використання", max_length=150)
    serial_number = models.CharField("Серійний номер", max_length=50)
    provider = models.CharField("Постачальник", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Прилад"
        verbose_name_plural = "Прилади"
