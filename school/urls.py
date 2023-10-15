from django.urls import path

from school import views

urlpatterns = [
    path("student_add/", views.student_add),
    path("students/", views.students),
]
