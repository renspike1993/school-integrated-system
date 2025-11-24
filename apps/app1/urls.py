from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='registrar'),
    
    
    path("students/", views.student_list, name="student_list"),
    path("students/create/", views.student_create, name="student_create"),
    path("students/<int:pk>/", views.student_detail, name="student_detail"),   # 👈 ADD THIS
    path("students/<int:pk>/edit/", views.student_update, name="student_update"),
    path("students/<int:pk>/delete/", views.student_delete, name="student_delete"),


    path('folders/', views.folder_list, name='folder_list'),
    path('folders/add/', views.folder_create, name='folder_create'),
    path('folders/<int:pk>/edit/', views.folder_update, name='folder_update'),
    path('folders/<int:pk>/delete/', views.folder_delete, name='folder_delete'),
]
