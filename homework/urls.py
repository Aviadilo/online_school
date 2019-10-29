from django.urls import path
from .views import *


app_name = 'homework'

urlpatterns = [
    path('', HomeworkCreateView.as_view()),
    # path('<int:pk>', HomeworkDetailView.as_view()),
    path('all', HomeworkListView.as_view()),
]
