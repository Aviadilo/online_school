from django.urls import path
from .views import *


app_name = 'course'

urlpatterns = [
    path('', CourseCreateView.as_view()),
    path('<int:pk>', CourseDetailView.as_view()),
    path('<int:pk>/users', CourseUsersView.as_view()),
    path('all', CourseListView.as_view()),
]
