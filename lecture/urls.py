from django.urls import path
from .views import *


app_name = 'lecture'

urlpatterns = [
    path('', LectureCreateView.as_view(), name='lecture-create'),
    path('<int:pk>', LectureDetailView.as_view(), name='lecture-detail'),
]
