
from django.urls import path
from .views import (
    NotificationListView, UnreadNotificationListView, NotificationDetailView, MarkAllAsReadView, NotificationStatsView,)



# ================================================================================
# urls notifications app
# ================================================================================
urlpatterns = [
    # get all notifications
    path('', NotificationListView.as_view(), name='notifications'),
    # get unread notification  :  read=False
    path('unread/', UnreadNotificationListView.as_view(), name='unread_notifications'),
    # get & update notifications just read  :  read:True
    path('<int:pk>/', NotificationDetailView.as_view(), name='update_or_get_notification'),
    # mark all notifications as read
    path('mark-all-read/', MarkAllAsReadView.as_view(), name='mark_all_read'),
    # get notifications status
    path('stats/', NotificationStatsView.as_view(), name='notification_stats'),
]
# ================================================================================