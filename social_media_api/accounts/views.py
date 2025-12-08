# ================================================================================# 
# ================================================================================
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .serializers import (RegisterSerializer, LoginSerializer, UserProfileSerializer, FollowActionSerializer)
User = get_user_model()
from .models import CustomUser
from notifications.models import Notification
# ================================================================================



# ================================================================================
# New user registration interface.
# Creates a new account, verifies data, and then issues JWT tokens to the user.
# User data is returned with a success message after registration is complete.
# ================================================================================
class UserRegisterView(generics.CreateAPIView):   
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserProfileSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            'message': 'User registered successfully'
        }, status=status.HTTP_201_CREATED)
# ================================================================================
# 
# 
# ================================================================================
# Login interface.
# Verifies user data, then issues new JWT tokens.
# Also returns the user profile with a login success message.
# ================================================================================
class UserLoginView(ObtainAuthToken):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': UserProfileSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            'message': 'User Login successfully'
        })
# ================================================================================
# 
# 
# ================================================================================
# An interface for viewing and updating the current user's profile.
# Allows the user to view or edit their data, as the returned object is request.user.
# ================================================================================
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserProfileSerializer
        return UserProfileSerializer
# ================================================================================
# 
# 
# ================================================================================
# User list display interface.
# Excludes the current user from results and supports name search.
# Also includes follow and unfollow functions for following or unfollowing users.
# ================================================================================
class UserListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserProfileSerializer
    
    def get_queryset(self):
        queryset = CustomUser.objects.all()
        queryset = queryset.exclude(id=self.request.user.id)
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(username__icontains=search)
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def follow_user(self, request, pk=None):
        user_to_follow = self.get_object()
        
        if user_to_follow == request.user:
            return Response(
                {'error': 'You cannot follow yourself'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not request.user.is_following(user_to_follow):
            request.user.follow(user_to_follow)
            message = f'You are now following {user_to_follow.username}'
            following = True
        else:
            message = f'You are already following {user_to_follow.username}'
            following = True
        
        return Response({
            'message': message,
            'following': following
        }, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def unfollow_user(self, request, pk=None):
        user_to_unfollow = self.get_object()
        
        if user_to_unfollow == request.user:
            return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.is_following(user_to_unfollow):
            request.user.unfollow(user_to_unfollow)
            message = f'You have unfollowed {user_to_unfollow.username}'
            following = False
        else:
            message = f'You are not following {user_to_unfollow.username}'
            following = False
        
        return Response({'message': message, 'following': following}, status=status.HTTP_200_OK)
# ================================================================================
# 
# 
# ================================================================================
# A dedicated interface for executing the follow process.
# Receives the user ID via Serializer, then checks:
# - Prevents self-following
# - Executes the follow if it doesn't exist
# - Sends a notification to the followed user
# Returns a clear message with the follow status.
# ================================================================================
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowActionSerializer
    
    def get_queryset(self):
        return CustomUser.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = serializer.validated_data['user_id']
        user_to_follow = get_object_or_404(User, id=user_id)

        if user_to_follow == request.user:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.user.is_following(user_to_follow):
            request.user.follow(user_to_follow)
            if comment.author != user:
             Notification.create_notification(
                recipient=user_to_follow,  
                actor=request.user,       
                verb='follow',     
                target=request.user     
            )
            return Response({
                'message': f'You are now following {user_to_follow.username}',
                'following': True,
                'user_id': user_id,
                'username': user_to_follow.username
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                'message': f'You are already following {user_to_follow.username}',
                'following': True,
                'user_id': user_id,
                'username': user_to_follow.username
            }, status=status.HTTP_200_OK)
# ================================================================================
# 
# 
# ================================================================================
# Unfollow interface.
# Receives user_id and checks:
# - Prevents self-unfollowing
# - Executes unfollowing only if the user is following
# Returns a message explaining the result and the follow status after the process.
# ================================================================================
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowActionSerializer
    
    def get_queryset(self):
        return CustomUser.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = serializer.validated_data['user_id']
        user_to_unfollow = get_object_or_404(User, id=user_id)
        if user_to_unfollow == request.user:
            return Response({'error': 'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        
        if request.user.is_following(user_to_unfollow):
            request.user.unfollow(user_to_unfollow)
            return Response({
                'message': f'You have unfollowed {user_to_unfollow.username}',
                'following': False,
                'user_id': user_id,
                'username': user_to_unfollow.username
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': f'You are not following {user_to_unfollow.username}',
                'following': False,
                'user_id': user_id,
                'username': user_to_unfollow.username
            }, status=status.HTTP_200_OK)
# ================================================================================
