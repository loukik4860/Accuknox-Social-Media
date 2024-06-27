# Accuknox-Social-Media
This project is a social media platform built using Django and Django Rest Framework. It includes user authentication, friend request functionality, and JWT-based token authentication.

## Project Structure

The project structure is as follows:

    socialMedia/
    │
    ├── account/
    │ ├── migrations/
    │ ├── init.py
    │ ├── admin.py
    │ ├── apps.py
    │ ├── models.py
    │ ├── serializers.py
    │ ├── urls.py
    │ ├── views.py
    │ └── renderers.py
    │
    ├── socialApp/
    │ ├── migrations/
    │ ├── init.py
    │ ├── admin.py
    │ ├── apps.py
    │ ├── models.py
    │ ├── serializers.py
    │ ├── urls.py
    │ ├── views.py
    │ └── renderers.py
    │
    ├── socialMedia/
    │ ├── init.py
    │ ├── asgi.py
    │ ├── settings.py
    │ ├── urls.py
    │ ├── wsgi.py
    │
    ├── manage.py
    ├── db.sqlite3
    └── README.md


## Features

- User Registration and Login
- JWT Authentication (Access and Refresh Tokens)
- Friend Request Management (Send, Accept, Reject)
- View Friend Requests (Pending, Accepted)
- Rate Limiting

## Requirements

- Python 3.x
- Django 5.0.6
- Django Rest Framework
- Django CORS Headers
- Django Filters
- SimpleJWT

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/socialMedia.git
   cd socialMedia

2. Create a virtual environment and activate it:

    ```bash 
    python -m venv venv
    source venv/bin/activate

3. Install the dependencies:

    ```bash
   pip install -r requirements.txt

4. Apply the migrations:

    ```bash
    python manage.py migrate

5. Create a superuser:

    ```bash
   python manage.py createsuperuser

6. Run the development server:

    ```bash
   python manage.py runserver

7. Access the admin panel at http://127.0.0.1:8000/admin/ and the API at http://127.0.0.1:8000/.

## API Endpoints

### Authentication

- Obtain Token: POST /api/token/
- Refresh Token: POST /api/token/refresh/
- Verify Token: POST /api/token/verify/

### User Management

- Register User: POST /user/register_user/
- Login User: POST /user/login_user/
- User Profile: GET /user/user_profile/
- Change Password: POST /user/change_password/
- Logout: POST /user/logout/
- List All Users: GET /user/all_user/

### Friend Request

- Send Friend Request: POST /post/friend_request/
- List All Friend Requests: GET /post/all_friend_request/
- Accept Friend Request: POST /post/friend_requests/<<int:pk>>/accept/
- Reject Friend Request: POST /post/friend_requests/<<int:pk>>/reject/
- List Pending Friend Requests: GET /post/user_friend_pending_list/<<int:pk>>/
- List Accepted Friend Requests: GET /post/user_friend_accepted_list/<<int:pk>>/

## Settings

### JWT Configuration

The JWT settings can be found in settings.py under the SIMPLE_JWT dictionary. You can configure token lifetimes, algorithms, and more.

### CORS Configuration

Allowed origins for CORS can be set in settings.py under the CORS_ALLOWED_ORIGINS list.
