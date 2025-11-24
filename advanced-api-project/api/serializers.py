# ============================================================================================
# Import necessary modules and models 
# ============================================================================================
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime
# ============================================================================================



# ============================================================================================
# Serializer for Book model: Handles book data serialization and validation
    # Converts Book instances to JSON format
    # Validates publication year to prevent future dates
    # Handles all book fields including author relationship
# ============================================================================================
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    # =========================================================================================
    # Custom validation for publication_year field
    # Ensures the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
# ============================================================================================



# ============================================================================================
# Serializer for Author model with custom nested representation of books
    # Converts Author instances to JSON format  
    # Includes nested book data using BookSerializer
    # Shows all books written by the author as nested objects
# ============================================================================================
class AuthorSerializer(serializers.ModelSerializer):
    # add new field to this serailzer of the books for just read 
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
# ============================================================================================



