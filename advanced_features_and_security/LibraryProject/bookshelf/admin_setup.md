# Django Admin Configuration for Book Model

## 1: Registered the Book Model

### In `bookshelf/admin.py`:

```bash
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
```

## 2: open terminal in root project 

### open call to create superUser

```bash
python manage.py createsuperuser
```
### create new super User 

```bash
Username: her create your usename
Email address:  her create your email valid
Password: create passwod ******** 
Password (again): confirm passwod ********
```
### Run the server

```bash
python manage.py runserver
```
### open browser and open this url admin control

```bash
http://127.0.0.1:8000/admin
```
