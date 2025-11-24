
# ==========================================================================
#  imports
# ==========================================================================
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book
# ==========================================================================


# ==========================================================================
# Book testing views GET POST PUT DELETE validation
# ==========================================================================
class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a new user for testing 
        self.user = User.objects.create_user(username='Mostafa', password='87654321')
        # Create a new author for testing
        self.author = Author.objects.create(name='Mostafa Bakhouya')
        # Create a new book for testing
        self.book = Book.objects.create(title='Test Book Added', publication_year=2023,  author=self.author)
        # Handle urls books ( GET, POST, PUT, PATCH, DELETE)
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.book_create_url = reverse('book-create')
        self.book_update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.book_delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # method handle test get all books
    def test_get_all_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book Added')
        self.assertEqual(response.data[0]['publication_year'], 2023)

    #  method handle test get detils item book
    def test_get_single_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book Added')
        self.assertEqual(response.data['publication_year'], 2023)

    #  method handle test create book with autehnticated
    def test_create_book_authenticated(self):
        # step 1: user login
        self.client.login(username='Mostafa', password='87654321')
        # data new book
        new_book = {'title': 'New Book', 'publication_year': 2024,  'author': self.author.id}
        # add new request POST to create new_book 
        response = self.client.post(self.book_create_url, new_book)
        # check if request status code successfully POST = Success = 201
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #  check if has 2 items count in objects databse books
        # check if has book title  'New Book' in databse books
        self.assertEqual(Book.objects.count(), 2)
        self.assertTrue(Book.objects.filter(title='New Book').exists())

    #  method handle test create book without login
    def test_create_book_unauthenticated(self):
        new_book = {'title': 'book can not create', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.post(self.book_create_url, new_book)
        #  check if request status code 401 mean error status 
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # method handle test update book with login
    def test_update_book_authenticated(self):
        #  user login
        self.client.login(username='Mostafa', password='87654321')
        #  update data
        update_data = {'title': 'Updated book for testing', 'publication_year': 2025,'author': self.author.id}
        response = self.client.put(self.book_update_url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title,  'Updated book for testing')
        self.assertEqual(self.book.publication_year, 2025)


    #  # method handle test delete book with login
    def test_delete_book_authenticated(self):
        self.client.login(username='Mostafa', password='87654321')
        response = self.client.delete(self.book_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)


    # method handle publication_year 
    def test_publication_year_validation(self):
        self.client.force_authenticate(user=self.user)
        invalid_book_data = {'title': 'book from futur',  'publication_year': 2030, 'author': self.author.id}
        response = self.client.post(self.book_create_url, invalid_book_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)
# ==========================================================================

# ==========================================================================
#  book test filtering, searching, ordering
# ==========================================================================
class BookFilterSearchOrderTestCase(APITestCase):
    def setUp(self):
        # Create 2 authors in database for testing
        self.author1 = Author.objects.create(name='Mostafa bakhouya')
        self.author2 = Author.objects.create(name='Bamoos mostafa')
        # Create 3 books in databse for testing
        self.book1 = Book.objects.create(title="book love and life", publication_year=2020, author=self.author1 )
        self.book2 = Book.objects.create(title='django story', publication_year=2022, author=self.author2)
        self.book3 = Book.objects.create(title='life in corona', publication_year=2023, author=self.author1)
        #  get all books list
        self.book_list_url = reverse('book-list')


    # test filter book use 'title'
    def test_filter_by_title(self):
        response = self.client.get(self.book_list_url, {'title': 'life'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    # test filter book use 'author'
    def test_filter_by_author(self):
        response = self.client.get(self.book_list_url, {'author': 'Mostafa'})       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    # test filter book use 'publication_year'
    def test_filter_by_publication_year(self):
        #  get all books published after 2021
        response = self.client.get(self.book_list_url, {'publication_year__gt': 2021})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)   # 2022 AND 2023 = publication_year__gt = 2021 < 2022 AND 2023

    # test searching
    def test_search_functionality(self):
        response = self.client.get(self.book_list_url, {'search': 'life'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    #  test ordering
    def test_ordering_functionality(self):
        #  order by publication year (old to new)
        response = self.client.get(self.book_list_url, {'ordering': 'publication_year'})        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)  # 2020 > 2022 > 2023        
        #  order by publication year (new to old)
        response = self.client.get(self.book_list_url, {'ordering': '-publication_year'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2023)  # 2023 > 2022 > 2020


    # test filter and ordering
    def test_combined_filter_search_order(self):
        #  filter , search, oredering
        response = self.client.get(self.book_list_url, {'author': 'mostafa', 'search': 'life',  'ordering': '-publication_year'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 
        self.assertEqual(response.data[0]['title'], 'life in corona')
# ==========================================================================



