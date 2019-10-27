from django.urls import path
from .views import *


app_name = 'lecture'

urlpatterns = [
    path('', LectureCreateView.as_view()),
    path('<int:pk>', LectureDetailView.as_view()),
    # path('<int:pk>/users', CourseUsersView.as_view()),
    # path('all', CourseListView.as_view()),
]
