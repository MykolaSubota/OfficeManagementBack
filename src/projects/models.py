from django.db import models
from django.conf import settings

class Project(models.Model):
    """
        Модель проекту
    """
    CATEGORY = (
        ('Teaching', 'Навчання'),
        ('Science', 'Наука'),
        ('Business', 'Бізнес')
    )
    title = models.CharField('Назва', max_length=250, unique=True)
    created_date = models.DateField('Дата створення', auto_now_add=True)
    description = models.TextField('Короткий опис', max_length=1000)
    category = models.CharField('Категорія', max_length=8, choices=CATEGORY, default='Teaching')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Автор",
        related_name="projects",
        null=True
    )
    performers = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Виконавці")

    def __str__(self):
        return self.title

    def tasks_count(self):
        return self.tasks.count()

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекти"

class Task(models.Model):
    """
        Модель завдання
    """
    title = models.CharField("Назва", max_length=250)
    created_date = models.DateField("Дата створення", auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Автор",
        related_name="tasks",
        null=True
    )
    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks_worker",
        verbose_name="Виконавець"
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект", related_name="tasks")
    deadline = models.DateTimeField("Дедлайн", blank=True, null=True)

    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"

    def __str__(self):
        return "{} - {}".format(self.performer, self.project)

class TimeFixation(models.Model):
    """
        Модель фіксації часу
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="timer_fixations", verbose_name="Назва")
    date = models.DateField("Дата", auto_now_add=True)
    begin = models.TimeField("Початок", auto_now_add=True)
    end = models.TimeField("Кінець", blank=True, null=True)
    duration = models.TimeField("Тривалість", blank=True, null=True)

    class Meta:
        verbose_name = "Фіксація часу"
        verbose_name_plural = "Фіксації часу"