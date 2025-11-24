# ==============================================================================
# imports
# ==============================================================================
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import BookFilter
# ==============================================================================


# ==============================================================================
# This view handles two main operations for the Author model:
# 1. GET  → Returns a list of all authors in the database.
# 2. POST → Creates a new author using the provided request data.
# ==============================================================================
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
# ==============================================================================






# =========================================================================================
# Get list all books for read & anyone can read this list without logged
# =========================================================================================
class BookListView(generics.ListAPIView):
    # get all books from databse 
    queryset = Book.objects.all() 
    # used Book serialzer 
    serializer_class = BookSerializer 
    # any one can used this list 
    permission_classes = [permissions.AllowAny] 
    # filter and searching
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # custom filter method
    filterset_class = BookFilter
    # fields can we searching with him
    search_fields = ['title', 'author', 'publication_year']
    # fields we can ordering with him
    ordering_fields = ['title', 'publication_year', 'author']
    # default ordering
    ordering = ['title'] 
# =========================================================================================
# 
# 
# 
# ==========================================================================================
# GET: get Book detials by id with RetrieveAPIView & anyone can read this list without logged
# ==========================================================================================
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  
    serializer_class = BookSerializer  
    permission_classes = [permissions.AllowAny]  
# ==========================================================================================
# 
# 
# 
# ==========================================================================================
# POST: create new Book with CreateAPIView & just authenticated can CREATE new book
# ==========================================================================================
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticated]

    # costum create book
    def perform_create(self, serializer):
        serializer.save()  
# ==========================================================================================
# 
# 
# 
# ==========================================================================================
# PUT, PATCH: Update Book item by id with UpdateAPIView & just authenticated can update item
# ==========================================================================================
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def perform_update(self, serializer):
        serializer.save() 
# ==========================================================================================
# 
# 
# ==========================================================================================
# DELETE: remove item book by id with destroyAPIView & just authenticaed can deleted
# ==========================================================================================
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all() 
    serializer_class = BookSerializer  
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly] 
# ==========================================================================================








