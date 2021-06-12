from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import Worker, Salary

@admin.register(Worker)
class WorkerAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'middle_name', 'email', 'phone', 'position', 'avatar')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    """
        Зарплата
    """
    list_display = ("worker", "salary")
    list_filter = ("worker", "salary")
    search_fields = ("worker",)
