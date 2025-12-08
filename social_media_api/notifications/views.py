# ================================================================================
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import (NotificationSerializer)
from django.contrib.auth import get_user_model
User = get_user_model()
# ================================================================================




# ================================================================================
# Displays all user notifications.
# Notifications are returned sorted from newest to oldest and are accessible only to the verified user.
# ================================================================================
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
# ================================================================================
# 
# 
# ================================================================================
# Displays only unread notifications.
# Helps the user see all new notifications that haven't been opened yet.
# ================================================================================
class UnreadNotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, read=False).order_by('-timestamp')
# ================================================================================
# 
# 
# ================================================================================
# Displays, updates, and deletes a specific notification.
# Used to view notification details, mark as read, or permanently delete a notification.
# Only notifications belonging to the user themselves can be accessed.
# ================================================================================
class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = NotificationSerializer(
            instance, 
            data=request.data, 
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data.get('read', False):
            instance.mark_as_read()
        
        return Response(serializer.data)
# ================================================================================
# 
# 
# ================================================================================
# An interface for marking all notifications as read at once.
# Useful when the user wants to filter and clean the notification inbox of unread notifications.
# ================================================================================
class MarkAllAsReadView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer
    
    def post(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        
        updated_count = notifications.update(is_read=True)
        
        return Response({
            'message': f'Marked {updated_count} notifications as read',
            'marked_read': updated_count
        }, status=status.HTTP_200_OK)
# ================================================================================
# 
# 
# ================================================================================
# An interface that returns notification statistics for the user.
# Includes the total number, the number of unread notifications, and the number of read notifications.
# Useful for displaying a badge or summary for the user within the front-end.
# ================================================================================
class NotificationStatsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        total = Notification.objects.filter(recipient=request.user).count()
        unread = Notification.objects.filter(recipient=request.user,read=False).count()
        
        return Response({
            'total_notifications': total,
            'unread_notifications': unread,
            'read_notifications': total - unread
        }, status=status.HTTP_200_OK)
# ================================================================================

