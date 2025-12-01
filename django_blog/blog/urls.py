from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView
)
from .views import add_comment, edit_comment, delete_comment
from .views import posts_by_tag, search_posts

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),



    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),    
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('posts/<int:post_id>/comment/add/', add_comment, name='comment_add'),
    path('comment/<int:comment_id>/edit/', edit_comment, name='comment_edit'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),


    path("search/", search_posts, name="search_posts"),
    path("tag/<str:tag_name>/", posts_by_tag, name="tag_posts"),
]
