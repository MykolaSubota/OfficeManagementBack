from django.contrib import admin
from src.projects.models import Project, Task, TimeFixation


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
        Проекти
    """
    list_display = ("title", "description", "category", "author", "created_date")
    filter_horizontal = ('performers',)
    list_filter = ("category", "performers", "author")
    search_fields = ("title",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
        Завдання
    """
    list_display = ("title", "author", "performer", "project", "created_date", "deadline")
    list_filter = ("author", "performer", "project")
    search_fields = ("title",)


@admin.register(TimeFixation)
class TimeFixationAdmin(admin.ModelAdmin):
    """
        Фіксації часу
    """
    list_display = ("task", "date", "duration")
    list_filter = ("task__title",)
    readonly_fields = ("task", "date", "duration")


admin.site.site_title = "Менеджмент наукового офісу"
admin.site.site_header = "Менеджмент наукового офісу"
