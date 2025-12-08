
from django.urls import path
from .views import (
    NotificationListView, UnreadNotificationListView, NotificationDetailView, MarkAllAsReadView, NotificationStatsView,)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications'),
    path('unread/', UnreadNotificationListView.as_view(), name='unread_notifications'),
    path('<int:pk>/', NotificationDetailView.as_view(), name='update_or_get_notification'),
    path('mark-all-read/', MarkAllAsReadView.as_view(), name='mark_all_read'),
    path('stats/', NotificationStatsView.as_view(), name='notification_stats'),
]