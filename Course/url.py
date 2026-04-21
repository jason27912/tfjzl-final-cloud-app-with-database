from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    # Correct path: 'submit' not 'submit_exam'
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    # Correct path format with submission_id
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
]
