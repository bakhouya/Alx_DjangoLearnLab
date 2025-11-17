# ================================================================
# imports
# ================================================================
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# ================================================================
# 
# 
# 
# ================================================================
# view book list
# ================================================================
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# ================================================================
# 
# 
# 
# ================================================================
# class modelViewSet to get all actions method [GET:list, GET:item POST, PUT, DELETE]
# just authenticated and admin user can access to this view 
# ================================================================
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
# ================================================================







