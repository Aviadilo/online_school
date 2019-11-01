from django.urls import path
from .views import *


app_name = 'course'

urlpatterns = [
    path('', CourseCreateView.as_view(), name='course-create'),
    path('<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('<int:pk>/users', CourseUsersView.as_view(), name='course-users'),
    path('all', CourseListView.as_view(), name='course-list'),
]
