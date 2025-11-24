

# Project Description
This project aims to build a professional API using the Django REST Framework to provide a comprehensive and scalable system for managing book and author data.

The project was designed according to modern software engineering principles, focusing on code organization, task isolation, and scalability.

# Key Project Features
## 1: A Logical and Well-Constructed View Structure:
The project utilizes a separate view system based on the type of operation required. Dedicated views are created for each operation:
    Displaying a Book List (GET List)
    Displaying a Specific Book (GET Detail)
    Adding a New Book (POST Create)
    Updating Book Data (PUT/PATCH Update)
    Deleting a Book (DELETE)

This separation provides the project with greater flexibility, ensuring each view performs a clear function without the complexity of combining operations into a single view.

## 2: Precise Data Control Using a Dedicated Serializer:
A professional Serializer is built for each Model with the following objectives:
    Define the data to be returned from the interface (Response)
    Control data coming from the user (Request)
    Manage relationships between models (ForeignKey and Nested Relationships)
    Implement validation rules within the Serializer itself to minimize errors and enhance data security

## 3: Advanced Filtering, Searching, and Sorting System:
Django Filter Backend was used to add advanced capabilities:
    Filter by title, author, or publication year
    Support for publication year ranges greater than/less than
    Comprehensive text search (SearchFilter)
    Sorting results (OrderingFilter)
    This allows users to obtain accurate results very quickly.

## 4: Permissions System Support:
To enhance security, a permissions system has been implemented that ensures:
    All users can read data (GET)
    Sensitive operations (POST, PUT, DELETE) are restricted to authenticated users only

## 5: Comprehensive Unit Tests for All Interfaces:
A wide range of tests has been built using APITestCase to verify:
    Status Codes are valid
    Returned Data is valid
    CRUD Operations are successful
    Filters, Searches, and Sorts are functioning correctly
    Authenticated vs. Unauthenticated Users are verified
    These tests ensure that the interface is stable, secure, and functions as expected.


# Installation & Setup Guide
### Installation 
### Repository cloning

````bash
git clone https://github.com/YourUsername/Alx_DjangoLearnLab.git
pipenv shell
cd advanced-api-project
````

### Setting requirements

````bash
pip install -r requirements.txt
````

### Database setup

````bash
python manage.py migrate
````

### Creating an administrative user (optional but important)
In terminal add this for create a new super user make sure create username and password 

````bash
python manage.py createsuperuser
````

### Running the local server

````bash
python manage.py runserver
````

## Setup Guide
### Books API Endpoints
````bash
GET /api/books/
# Retrieves a complete list of all books in the database.
# Supports filtering, searching, and ordering for flexible querying.

POST /api/books/create/
# Creates a new book entry.
# Requires authentication to ensure only authorized users can add books.

GET /api/books/<int:pk>/
# Retrieves detailed information about a specific book identified by its ID.
# Useful for displaying full information on a single record.

PUT /api/books/<int:pk>/update/
# Fully updates all fields of the selected book.
# Requires authentication to maintain data integrity.

PATCH /api/books/<int:pk>/update/
# Partially updates selected fields of a specific book.
# Suitable for small modifications without replacing all data.

DELETE /api/books/<int:pk>/delete/
# Deletes a specific book from the database permanently.
# Protected by authentication to prevent unauthorized deletions.
````


# Filtering — Searching — Ordering
This section explains how the API handles filtering, searching, and sorting the book list, with practical examples of how to submit requests via URL.

## Filtering
Filtering has been enabled so that the user can filter the list of books based on several criteria.

### Filter by title
The search within the title is for any part of the text, without sensitivity to the case of the letters.

````bash
GET /api/books/?title=life
# Return all books whose title contains the word "life".
# Life in Corona
# Book of Life
````

### Filter by author name
The search is performed within the author's name, in a case-insensitive manner.

````bash
GET /api/books/?author=mostafa
# He returns all books whose author belongs to a name containing the word "mostafa".
````

### Publication Year Filtering
Exact match

````bash
GET /api/books/?publication_year=2020
# He is re-publishing books from 2020.
````

Greater Than

````bash
GET /api/books/?publication_year__gt=2020
# He is re-publishing books that were released after 2020.
````

Less Than

````bash
GET /api/books/?publication_year__lt=2020
# It reissues books published before 2020.
````

Greater or Equal

````bash
GET /api/books/?publication_year__gte=2021
# Re-published books from 2021 or later.
````

Less or Equa

````bash
GET  /api/books/?publication_year__lte=2023
# Re-published books from 2023 or earlier.
````


## Search
The search works across multiple fields simultaneously, where the following are used '?search='

````bash
GET /api/books/?search=life
# It searches for the word "life" within: Title, Author's Name, Year of Publication
# and returns all matching results.
````

## Ordering
The results can be sorted in ascending or descending order using '?ordering='

### Sort by year of publication — ascending

````bash
GET /api/books/?ordering=publication_year
# It displays books from oldest to newest.
````

### Sort by year of publication — descending

````bash
GET /api/books/?ordering=-publication_year
# It displays books from newest to oldest.
````

### Sort by title

````bash
GET /api/books/?ordering=title
````

## Combining filtering, searching, and sorting
All these processes can be combined into a single request.

````bash
GET /api/books/?author=mostafa&search=life&ordering=-publication_year
# Search for an author whose name contains "mostafa"
# Search within books for text containing "life"
# Results are sorted from newest to oldest
````

# Summary:
The project offers a simple and structured book management API that includes all CRUD operations with path customization, along with support for filtering, searching, and sorting. A data validation system and comprehensive testing are also included to ensure performance quality. The project demonstrates a clear and practical application of Django REST Framework concepts in a clean and scalable way.