
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Notification
from .serializers import (NotificationSerializer)
from django.contrib.auth import get_user_model
User = get_user_model()


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-created_at')


class UnreadNotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user, read=False).order_by('-created_at')


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

