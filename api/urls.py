from django.urls import path
from . import views

urlpatterns = [
    path('dummy/', views.dummy_view, name='dummy'),
    path('users/', views.create_user, name='create user'),
    path('courses/', views.courses, name='courses'),
    # path('courses/', views.getCourses, name='get courses'),
    path('courses/<int:course_id>/', views.getCourse, name='get a course')
]