# Social Media API
A social networking platform built using the Django REST Framework, enabling users to create an account, log in, add posts, comment on them, like them, and follow other users to see their posts.

## Key Features
### Authentication
Register a new account
Login
Use JWT Tokens to access the API
Manage your account and update your user profile

### Posts
Any user can post a new post
View all posts or posts from a specific user
Edit and delete posts belonging to the account owner

### Comments
Any user can comment on any post
Edit and delete their own comments only

### Likes
Users can like any post
They can also unlike a post

### Follow System
Users can follow any other user
When following someone, they see their posts in the Feed
An Unfollow system is also available

### Feed Page
Displays posts from users the account owner follows
Sorted from newest to oldest

### Project Architecture
The project is built Based on:
Django
Django REST Framework
SimpleJWT for authentication
SQLite/PostgreSQL database
Professional separation of Models/Serializers/Views