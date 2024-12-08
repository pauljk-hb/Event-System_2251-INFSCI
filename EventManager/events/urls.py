from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("events/", views.events, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/old', views.history_events, name='history_events'),

]