from django.urls import path
from .views import *


app_name = 'homework'

urlpatterns = [
    path('', HomeworkCreateView.as_view(), name='homework-create'),
    path('<int:pk>', HomeworkDetailView.as_view(), name='homework-detail'),
    path('<int:pk>/mark', HomeworkMarkDetailView.as_view(), name='homework-mark'),
    path('<int:pk>/comment', CommentCreateView.as_view(), name='comment-create'),
    path('all', HomeworkListView.as_view(), name='homework-list'),
]
