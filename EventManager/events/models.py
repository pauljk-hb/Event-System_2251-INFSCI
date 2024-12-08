from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Event(models.Model):
   event_id = models.AutoField(primary_key=True)
   title = models.CharField(max_length=255)
   description = models.TextField()
   time = models.DateTimeField()
   location = models.CharField(max_length=255)
   type = models.CharField(max_length=50)
   tags = models.CharField(max_length=255)
   latitude = models.FloatField(null=True, blank=True)
   longitude = models.FloatField(null=True, blank=True)
   organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='events', null=True, blank=True)

  
   def __str__(self):
       return self.title


class EventSignup(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='signups')
    signup_date = models.DateTimeField(auto_now_add=True)
