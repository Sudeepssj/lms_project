from django.urls import path
from .views import *
urlpatterns = [
    path('instructor/', instructor_dashboard, name='instructor_dashboard'),
    path('add/', add_course),
    path('edit/<int:id>/', edit_course),
    path('delete/<int:id>/', delete_course),
    path('profile/', instructor_profile, name='instructor_profile'),
    path('enroll/<int:id>/', enroll_course, name='enroll'),
    path('student/profile/', student_profile, name='student_profile'),

]