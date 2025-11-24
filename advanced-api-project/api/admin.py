from django.contrib import admin
from .models import Author, Book



# ======================================================================================
# Registering Author and Book models to the amin site
# ======================================================================================
admin.site.register(Author)
admin.site.register(Book)
# ======================================================================================
