# Project Description
The Django Blog project is a simple yet powerful blogging platform built on the Django framework. It allows users to create, manage, comment on, and organize posts using tags. It also features an advanced search system that enables readers to easily find posts using keywords or tags.
The project aims to provide a comprehensive tutorial covering the fundamentals of creating a professional blog using Django, while implementing best practices in structuring, data management, forms, and interfaces.

# Key Features
## 1: The Complete Notation System (CRUD)
### Create articles
### Edit articles
### Delete articles
### View individual article details

## 2. Comment System with User Management
### Adding comments to articles
### Editing comments (only the author can edit them)
### Deleting comments (only the author can delete them)
### Linking comments to registered users

## 3. Tags using django-taggit
### Adding tags to articles during creation or editing
### Displaying tags within the article page
### Clicking on a tag displays all related articles

## 4. Advanced Article Search
### Searching by tags
### Displaying a professionally organized search results page

## 5. Filtering articles by tags
### A dedicated page displaying articles with the same tag

## 6. Simple and organized HTML interfaces
### Using Django templates
### Displaying articles with a clean and clear design

## 7. Complete project documentation
### Explanation of all features
### File organization
### Specification of system requirements

## Project structure
````bash
django_blog/
│
├── blog/
│ │
│ ├── migrations/            
│ ├── templates/
│ │   └── blog/              
│ │       ├── base.html
│ │       ├── login.html
│ │       ├── logout.html
│ │       ├── post_confirm_delete.html
│ │       ├── post_detail.html
│ │       ├── post_form.html
│ │       ├── posts_list.html
│ │       ├── profile.html
│ │       ├── register.html
│ │       ├── search_results.html     
│ │       └── tag_posts.html
│ │             
│ ├── static/
│ │   └── blog/              
│ │       ├── css/
│ │       │     └── style.css
│ │       └── js/
│ │             └── script.js
│ │         
│ ├── models.py              
│ ├── views.py               
│ ├── urls.py                
│ ├── forms.py               
│ └── admin.py               
│
├── django_blog/
│ │
│ ├── settings.py            
│ ├── urls.py                
│ ├── wsgi.py               
│ └── asgi.py                
│
├── Requirements.txt
├── README.md
└── manage.py                

````
## Requirements
Python 3.10+
Django 5+
django-taggit

# Operating steps
## Setting requirements
````bash
# Clone repositry from github
git clone https://github.com/bakhouya/Alx_DjangoLearnLab.git
# go to the path project
cd django blog
# install and activate virtual enviroment
pipenv install & pipenv shell
# install requirements
pip install -r requirements.txt
# migrate databse
python manage.py migrate
# create new super user
python manage.py createsuperuser
# run server
python manage.py runserver
````

# Explanation of URL paths in the project (URLs Documentation)
The blog project contains a set of URLs that organize the login process, account management, creating, editing, deleting, and interacting with posts through comments, as well as search and tags. A detailed explanation of each URL follows:

## 1: Authentication & Profile Paths and Account Management
|  Route        | Description | 
|  :---         | :---        | 
|  "/login"     | Displays the login form using LoginView and the **login.html** template. |
| "/logout"     | Logs the user out and displays the **logout.html** template. |
| "/register"   | Allows the user to create a new account using the **register_view** function. |
| "/profile"    | Displays the user's profile page using the **profile_view** function. |

## 2: Post Paths
|  Route                      | Description | 
|  :---                       | :---        | 
|  "/posts/"                  | Displays all posts using **PostListView**. |
| "/post/new/"                | Allows creating a new post via **PostCreateView**. |
| "/post/<int:pk>/"           | Displays details of a specific post via **PostDetailView**. |
| "/post/<int:pk>/update/"    | Allows updating a post via **PostUpdateView**. |
| "/post/<int:pk>/delete/"    | Deletes a specific post via **PostDeleteView**. |

## 3: Comment Paths
|  Route                           | Description | 
|  :---                            | :---        | 
|  "/post/<int:pk>/comments/new/"  | Create a new comment on a specific article using **CommentCreateView**. |
| "/comment/<int:pk>/update/"      | Edit an existing comment using **CommentUpdateView**. |
| "/comment/<int:pk>/delete/"      | Delete a comment using **CommentDeleteView** |

## 4: Search and Tags
|  Route                           | Description | 
|  :---                            | :---        | 
|  "/search/"                      | Search within articles by title, content, or tags using the **search_posts** function. |
| "/tags/<slug:tag_slug>/"         | Display all articles associated with a specific tag using **PostByTagListView**. |


## Author
This project was developed as part of the Django Framework Learning Tasks within the ALX Django Learn Lab project.

## License 
This project is for educational purposes and can be used and developed freely.