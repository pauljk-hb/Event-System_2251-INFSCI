#models
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_event_manager = models.BooleanField(default=False) # Indicates if the user is an Event Manager