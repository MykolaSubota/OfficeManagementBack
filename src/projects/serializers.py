from rest_framework import serializers

from .models import Project, Task, TimeFixation
from ..base.serializers import AllListSerializer


class CreateTaskSerializer(serializers.ModelSerializer):
    """
        Створення завдання в проекті
    """

    class Meta:
        model = Task
        fields = ("title", "created_date", "author", "performer", "project", "deadline")


class ListTasksSerializer(serializers.ModelSerializer):
    """
        Список завдань в проекті
    """

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = AllListSerializer
        model = Task
        fields = ("id", "title", "created_date", "author", "performer", "project", "deadline", "timer_fixations")



class ProjectSerializer(serializers.ModelSerializer):
    """
        Вивід і редагування проекту
    """
    author = serializers.ReadOnlyField(source='author.username')
    tasks = ListTasksSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ("id", "created_date", "title", "tasks", "description", "category", "author", "performers")


class ListProjectSerializer(serializers.ModelSerializer):
    """
        Список проектів
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Project
        fields = ("id", "created_date", "title", "category", "author", "performers")


class CreateTimeFixationSerializer(serializers.ModelSerializer):
    """
        Створення фіксатора часу до завдання
    """

    class Meta:
        model = TimeFixation
        fields = ("task", "date", "begin", "end", "duration")



class ListTimeFixationSerializer(serializers.ModelSerializer):
    """
        Список фіксаторів часу в завданні
    """

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = AllListSerializer
        model = TimeFixation
        fields = ("task", "date", "begin", "end", "duration")

