from rest_framework import permissions, generics, mixins, viewsets

from ..base.classes import CreateUpdateDestroy, CreateRetrieveUpdateDestroy, MixedPermission
from ..base.permissions import IsAuthor, IsPerformer
from .models import Project, Task, TimeFixation
from .serializers import ProjectSerializer, CreateTaskSerializer, CreateTimeFixationSerializer, ListTasksSerializer

class ProjectListView(generics.ListAPIView):
    """
        Список проектів
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(CreateRetrieveUpdateDestroy):
    """
        Створення, редагування, видалення проектів
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class TaskListView(mixins.RetrieveModelMixin, MixedPermission, viewsets.GenericViewSet):
    """
        Створення, редагування, видалення завдань
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = ListTasksSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny]}

class TaskView(CreateUpdateDestroy):
    """
        Створення, редагування, видалення завдань
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

class TimeFixationView(CreateUpdateDestroy):
    """
        Створення, редагування, видалення фіксаторів часу
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TimeFixation.objects.all()
    serializer_class = CreateTimeFixationSerializer
    permission_classes_by_action = {'update': [IsPerformer],
                                    'destroy': [IsPerformer]}

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
