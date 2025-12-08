from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
User = get_user_model()


# =====================================================================================
#  test follers feature 
# =====================================================================================
class FollowSystemTest(TestCase):
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
        self.client.force_authenticate(user=self.user1)
    # test follow user
    def test_follow_user(self):
        url = f'/api/accounts/follow/{self.user2.id}/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user1.is_following(self.user2))
    # test can not follow my self
    def test_cannot_follow_self(self):
        url = f'/api/accounts/follow/{self.user1.id}/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    # test unfollow user
    def test_unfollow_user(self):
        self.user1.follow(self.user2)
        
        url = f'/api/accounts/unfollow/{self.user2.id}/'
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(self.user1.is_following(self.user2))
# =====================================================================================

