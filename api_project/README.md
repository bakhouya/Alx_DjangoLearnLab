# Django REST API Project

A complete Django REST Framework (DRF) educational project that demonstrates:
API creation (ListAPIView)
CRUD operations using ViewSets & Routers
Token Authentication
Permissions
Clean project structure
How to run & test all endpoints

This README explains every step from cloning the repository, installing dependencies, running the server, and testing each API endpoint.

## Project Description

This project is part of the ALX Django Learning Lab, where we build a professional API using Django REST Framework with authentication and permissions.
The API manages Book objects and supports:
Create
Read
Update
Delete
Token-protected endpoints

## How to Clone the Project
### Clone the repository

````bash
git clone https://github.com/bakhouya/Alx_DjangoLearnLab.git
````
### Move to the project directory

````bash
cd Alx_DjangoLearnLab/api_project
````

## Setup Virtual Environment (pipenv)

````bash
pip install pipenv
pipenv install
pipenv shell
````
## Install Required Dependencies

````bash
pip install django djangorestframework 
````
Installed packages:
    Django
    Django REST Framework

## Apply Migrations

````bash
python manage.py makemigrations
python manage.py migrate
````

## Create Superuser

````bash
python manage.py createsuperuser
````

## Run Development Server 

````bash
python manage.py runserver
````
## Project Structure Overview

````bash
api_project/
├── api/
│ ├── models.py             # Book model
│ ├── serializers.py        # BookSerializer
│ ├── views.py              # BookList + BookViewSet
│ ├── urls.py               # API routes
│
├── api_project/
│ ├── settings.py # Django + DRF config
│ ├── urls.py # Main URL router
│
├── manage.py
````

## API Endpoints Documentation
### Get Authentication Token 

````bash
# open this urls in your browser or postman
POST http://127.0.0.1:8000/api/auth/token/

# Body:
{
    "username": "admin",  # change this value to your usename 
    "password": "123456"  # change this value to your password
}

# Response
{
    "token": "a88ff9e92b..."
}
````

### List Books (ListAPIView)

````bash
# open this urls in your browser or postman
GET http://127.0.0.1:8000/api/books/

# Response
[
    {
        "id": 1,
        "title": "Book Title",
        "author": "Author Name"
    }
]
````


### Authentication & Permissions
To authenticate, send this header:
````bash
Authorization: Token <token>
````

### CRUD Endpoints – ViewSet
````bash
#  List Books
GET http://127.0.0.1:8000/api/books_all/

#  Retrieve Book
GET http://127.0.0.1:8000/api/books_all/<id>/

#  Create Book
POST http://127.0.0.1:8000/api/books_all/
{
  "title": "new title book",
  "author": "author book"
}

#  Delete Book
DELETE http://127.0.0.1:8000/api/books_all/<id>/

#  Update Book
PUT | PATCH http://127.0.0.1:8000/api/books_all/<id>/
{
  "title": "update title book",
  "author": "update author book"
}

````



# Final Notes

This project demonstrates:
DRF fundamentals
Serialization
ViewSets & Routers
Token authentication
Permissions
It is clean, simple, and easy to extend for bigger projects.

