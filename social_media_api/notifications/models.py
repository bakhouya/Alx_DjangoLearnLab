# notifications/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('follow', 'New Follower'),
        ('like', 'Post Liked'),
        ('comment', 'New Comment'),
    ]
    
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='actions', null=True, blank=True)
    verb = models.CharField(max_length=50, choices=NOTIFICATION_TYPES)
    
    target_content_type = models.ForeignKey( ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_object_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')

    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', 'read']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"{self.verb} notification for {self.recipient.username}"

    @classmethod
    def create_notification(cls, recipient, actor, verb, target=None):
        notification = cls.objects.create(
            recipient = recipient,
            actor = actor,
            verb = verb,
        )
        
        if target:
            notification.target = target
            notification.save()
        
        return notification
