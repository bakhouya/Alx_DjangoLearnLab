
# ================================================================
# imports
# ================================================================
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token
# ================================================================
# 
# 
# 
# ================================================================
# urls router default to handle group of urls for modelViewSet
# ================================================================
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
# ================================================================
# 
# 
# 
# ================================================================
# urls app api 
# ================================================================
urlpatterns = [
    # url auth token
    path('auth/token/', obtain_auth_token, name='api_token_auth'),
    # url get all book list from view BookList
    path('books/', BookList.as_view(), name='book-list'),
    # url handle all method books_all from modelViewSet
    path('', include(router.urls)),
]
# ================================================================

