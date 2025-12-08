from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

User = get_user_model()

class FeedTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(
            username='user1',
            email='user1@test.com',
            password='password123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            email='user2@test.com',
            password='password123'
        )
        
        self.post1 = Post.objects.create(
            author=self.user2,
            title='Post by User 2',
            content='Test content'
        )
        
        self.client.force_authenticate(user=self.user1)
    
    def test_feed_without_following(self):
        url = '/api/posts/feed/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 0)
    
    def test_feed_with_following(self):
        self.user1.follow(self.user2)
        
        url = '/api/posts/feed/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
