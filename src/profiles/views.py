from rest_framework.generics import get_object_or_404

from .models import Worker
from .serializers import GetWorkerSerializer
from rest_framework import permissions, generics
from rest_framework.viewsets import ModelViewSet

class WorkerPublicView(ModelViewSet):
    """Вивід публічного профіля працівника"""
    queryset = Worker.objects.all()
    serializer_class = GetWorkerSerializer
    permission_classes = [permissions.AllowAny]

class WorkerPrivateView(generics.RetrieveUpdateAPIView):
    """Вивід профіля працівника"""
    serializer_class = GetWorkerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Worker.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request):
        return self.retrieve(request)
