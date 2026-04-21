from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('lesson/<int:lesson_id>/take/', views.take_exam, name='take_exam'),
    path('lesson/<int:lesson_id>/submit/', views.submit_exam, name='submit_exam'),
    path('results/<int:submission_id>/', views.show_exam_results, name='show_exam_results'),
]
