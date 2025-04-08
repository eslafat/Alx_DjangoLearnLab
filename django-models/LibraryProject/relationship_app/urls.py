from . import views
from django.urls import path


urlpatterns = [
    path('books/', views.books_view, name = 'book_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]