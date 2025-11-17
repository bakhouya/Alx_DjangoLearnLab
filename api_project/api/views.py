# ================================================================
# imports
# ================================================================
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
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
class BookList(ListAPIView):
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
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
# ================================================================







