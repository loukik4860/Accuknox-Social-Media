from django.urls import path, include
from .views import userRegistrationView, UserLoginView, UserProfileView, UserPasswordChange, LogoutView, allUsersView

urlpatterns = [
    path("all_user/", allUsersView.as_view(), name="all_user"),
    path("register_user/", userRegistrationView.as_view(), name="register"),
    path("login_user/", UserLoginView.as_view(), name="userLogin"),
    path("user_profile/", UserProfileView.as_view(), name="user_profile"),
    path("change_password/", UserPasswordChange.as_view(), name="password_change"),
    path("logout/", LogoutView.as_view(), name="logout")
]
