from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet, CommentViewSet, FeedView,
    LikePostView, UnlikePostView, PostLikesView,
    )
# ================================================================================
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
# ================================================================================

# ================================================================================
# urls posts app
# ================================================================================
urlpatterns = [
    # include urls default to handle GRUD posts
    path('', include(router.urls)),
    # get feed
    path('feed/', FeedView.as_view(), name='feed'),
    # like post
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    # unlike post
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    # get likes post
    path('<int:pk>/likes/', PostLikesView.as_view(), name='post-likes'),
]
# ================================================================================