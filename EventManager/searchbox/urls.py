from django.urls import path
from .views import event_search  # Import the view function

urlpatterns = [
    path("", event_search, name="event_search"),  # This points to the search functionality
]