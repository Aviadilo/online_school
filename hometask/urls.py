from django.urls import path
from .views import *


app_name = 'hometask'

urlpatterns = [
    path('', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]
