from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='app3_index'),
    path('print/<int:doc_id>/', views.print_document, name='print_document'),
]
