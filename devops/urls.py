from django.urls import path 
from devops import views

urlpatterns = [
    path('home/', views.home),
    path('student/<st_id>', views.getStudent),
    path('all', views.getALLStudents),
    path('new', views.newStudent),
    path('edit/<st_id>', views.editstudent),
    path('delete/<st_id>', views.deletestudent)

    ]
