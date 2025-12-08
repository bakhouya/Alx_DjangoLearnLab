
from django.urls import path
from .views import (UserRegisterView, UserLoginView, UserProfileView,UserListView, FollowUserView, UnfollowUserView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# =====================================================================================
urlpatterns = [
    # default jwt token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Post register new user
    path('register/', UserRegisterView.as_view(), name='register'),
    # Custom login user
    path('login/', UserLoginView.as_view(), name='login'),
    # get & update profile
    path('profile/', UserProfileView.as_view(), name='profile'),
    # get all users
    path('users/', UserListView.as_view(), name='users'),
    # follow user
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    # unfollow user
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
# =====================================================================================
