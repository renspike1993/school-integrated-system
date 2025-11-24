from django.urls import path

from . import views
from apps.app1 import views as student_list

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.index, name='library'),    
    path('opac/', views.opac, name='opac'),
    path('list/', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('<int:pk>/edit/', views.book_update, name='book_update'),
    path('<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('borrow-books/<int:student_id>/', views.borrow_book_list, name='borrow_book_list'),
    path("books/<int:pk>/barcode/add/", views.bookbarcode_create, name="bookbarcode_create"),
    path(
        'borrow-books/<int:student_id>/<int:book_id>/<int:barcode_id>/borrow/',
        views.borrow_book,
        name='borrow_book'
    ),
    path('borrowed/<int:borrowed_id>/return/', views.return_book, name='return_book'),

    path('books/borrow-history/', views.all_books_borrow_history, name='all_books_borrow_history'),

    path('students/', student_list.student_list, name='library_students'),
    path("students/<int:pk>/", student_list.student_detail, name="student_detail"),   # 👈 ADD THIS
        
    path(
        "books/<int:book_id>/barcode/<int:barcode_id>/delete/",
        views.bookbarcode_delete,
        name="bookbarcode_delete",
    ),
    path('logs/', views.security_logs, name='security_logs'),
    
    path("borrowed/all/", views.all_borrowed_books, name="borrowed_all"),
    path('api/check-book/<str:barcode>/', views.api_check_book_status, name='check-book-api'),
    
    path('ads/', views.ads, name='ads'),
    


    # ------------------------------- COLLECTIONS -------------------------------
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/create/', views.collection_create, name='collection_create'),
    path('collections/<int:pk>/', views.collection_detail, name='collection_detail'),
    path('collections/<int:pk>/update/', views.collection_update, name='collection_update'),
    path('collections/<int:pk>/delete/', views.collection_delete, name='collection_delete'),

    path('manual/', views.manual, name='manual'),
    path('book/views', views.book_views, name='book_views'),

    path("api/reservations/", views.api_reservations, name="api_reservations"),
    path('book/<int:pk>/marc21/', views.book_marc21_view, name='book_marc21'),
    path('book/<int:pk>/isbd/', views.book_isbd, name='book_isbd'),
    path('faker-book/', views.generate_fake_books_view, name='generate_fake_books'),

    ]
