from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.WorkerPrivateView.as_view()),
    path('profile/<int:pk>/', views.WorkerPublicView.as_view({'get': 'retrieve'})),
]
