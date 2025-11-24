


# ==============================================================================
# imports
# ==============================================================================
from django.urls import path
from . import views
# ==============================================================================



# ==============================================================================
# urld app api
# ==============================================================================
urlpatterns = [
    # for GET and POST authors
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),

    # -------------------------- start urls handle books--------------------------
    path('books/', views.BookListView.as_view(), name='book-list'),  
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  
    path('books/create/', views.BookCreateView.as_view(), name='book-create'), 
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'), 
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    # -------------------------- end urls handle books --------------------------
    
]
# ==============================================================================
