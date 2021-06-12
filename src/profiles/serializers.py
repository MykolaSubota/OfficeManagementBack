from rest_framework import serializers
from .models import Worker

class GetWorkerSerializer(serializers.ModelSerializer):
    """Вивід інформації про працівника"""
    class Meta:
        model = Worker
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "date_joined",
            "user_permissions"
        )

