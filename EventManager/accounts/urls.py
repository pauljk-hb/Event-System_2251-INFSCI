from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("event_manager_profile/", views.event_manager_profile, name="event_manager_profile"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path('create_event/', views.event_manager_profile, name='create_event'),
]