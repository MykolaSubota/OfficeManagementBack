from django.urls import path
from . import views

urlpatterns = [
    path('task', views.TaskView.as_view({'post': 'create'})),
    path('task/<int:pk>', views.TaskListView.as_view({'get': 'retrieve'})),
    path('task/<int:pk>', views.TaskView.as_view({'put': 'update', 'delete': 'destroy'})),
    path('project', views.ProjectView.as_view({'post': 'create'})),
    path('project/<int:pk>', views.ProjectView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', views.ProjectListView.as_view()),
    path('time_fixation', views.TimeFixationView.as_view({'post': 'create'})),
    path('time_fixation/<int:pk>', views.TimeFixationView.as_view({'put': 'update', 'delete': 'destroy'})),
]

