from django.contrib import admin
from src.reagents_devices.models import Reagent, Device

@admin.register(Reagent)
class ReagentAdmin(admin.ModelAdmin):
    """
        Реагенти та матеріали
    """
    list_display = (
        "name",
        "characteristic",
        "amount",
        "placing",
        "producer",
        "valid_until",
        "field_of_use",
        "provider"
    )
    list_filter = ("name", "placing", "producer", "field_of_use", "provider")
    search_fields = ("name", "placing", "producer", "field_of_use", "provider")

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """
        Прилади
    """
    list_display = (
        "name",
        "producer",
        "amount",
        "placing",
        "year_of_purchase",
        "date_of_last_inspection",
        "field_of_use",
        "serial_number",
        "provider"
    )
    list_filter = ("name", "placing", "field_of_use", "provider")
    search_fields = ("name", "placing", "year_of_purchase", "field_of_use", "provider")
