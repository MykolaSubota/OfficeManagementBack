from rest_framework import serializers

class AllListSerializer(serializers.ListSerializer):
    """
        Всі компоненти
    """
    def to_representation(self, data):
        return super().to_representation(data)
