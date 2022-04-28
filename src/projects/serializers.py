from rest_framework import serializers
from ..profiles.serializers import GetWorkerSerializer
from datetime import datetime
from .models import Project, Task, TimeFixation
from ..base.serializers import AllListSerializer

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
        fields = ("id","task", "date", "start", "stop", "duration")

class ListProjectSerializer(serializers.ModelSerializer):
    """
        Список проектів
    """
    author = GetWorkerSerializer(read_only=True)
    performers = GetWorkerSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ("id", "created_date", "title", "category", "author", "performers")

class ListTasksSerializer(serializers.ModelSerializer):
    """
        Список завдань в проекті
    """

    author = GetWorkerSerializer(read_only=True)
    performer = GetWorkerSerializer(read_only=True)
    project = ListProjectSerializer(read_only=True)
    timer_fixations = ListTimeFixationSerializer(many=True, read_only=True)

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = AllListSerializer
        model = Task
        fields = ("id", "title", "created_date", "author", "performer", "project", "deadline", "timer_fixations")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "created_date", "title", "description", "category", "author", "performers")

class GetProjectSerializer(serializers.ModelSerializer):
    """
        Вивід і редагування проекту
    """
    author = GetWorkerSerializer(read_only=True)
    tasks = ListTasksSerializer(many=True, read_only=True)
    performers = GetWorkerSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ("id", "created_date", "title", "tasks", "description", "category", "author", "performers")


class ListProjectSerializer(serializers.ModelSerializer):
    """
        Список проектів
    """
    author = GetWorkerSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ("id", "created_date", "title", "category", "author", "performers")


class CreateTimeFixationSerializer(serializers.ModelSerializer):
    """
        Створення фіксатора часу до завдання
    """
    # start = ''TimeFixation.start
    # stop = TimeFixation.stop
    # duration = stop.strftime('%H:%M:%S.%f').time() - start.strftime('%H:%M:%S.%f').time()
    class Meta:
        model = TimeFixation
        fields = ("task", "date", "duration")

class CreateTaskSerializer(serializers.ModelSerializer):
    """
        Створення завдання в проекті
    """

    class Meta:
        model = Task
        fields = ("title", "created_date", "author", "performer", "project", "deadline")

