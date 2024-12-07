from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("events/", views.events),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]