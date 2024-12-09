
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import EventSignup, Event
from django.contrib.auth.models import User


# View for user registration
# Handles GET (show form) and POST (process registration)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # log user in after registering
            if user.is_event_manager:
                return redirect('event_manager_profile') # Redirect Event Managers to their profile
            else:
                return redirect('user_profile') # Redirect standard users to their profile
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# View for user login
# Authenticates credentials and redirects based on role
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_event_manager:
                return redirect('event_manager_profile')
            else:
                return redirect('user_profile')

    return render(request, 'accounts/login.html')

# Logs out the current user and redirects to the login page
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile page for Event Managers
# Only accessible to users with is_event_manager = True
@login_required
def event_manager_profile(request):
    if not request.user.is_event_manager:
        return redirect('user_profile')

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        time = request.POST['time']
        event_type = request.POST['type']
        tags = request.POST['tags']

        # Erstellen eines neuen Event-Objekts
        event = Event(
            title=title,
            description=description,
            location=location,
            time=time,
            type=event_type,
            tags=tags,
            latitude= 40.4406,
            longitude= -79.9959,
            organizer=request.user
            )

        # Speichern des Event-Objekts in der Datenbank
        event.save()

        messages.success(request, 'Event created successfully!')
        return redirect('event_manager_profile')
    
    user = request.user
    events = Event.objects.filter(organizer=request.user)

    return render(request, 'accounts/event_manager_profile.html', {'user': user, 'events': events})

# Profile page for standard users
# Only accessible to users with is_event_manager = False
@login_required
def user_profile(request):
    user = request.user
    signups = EventSignup.objects.filter(user=user).select_related('event')
    events = [signup.event for signup in signups]

    if request.method == 'POST' and 'cancel_signup' in request.POST:
        event_id = request.POST['event_id']
        event = Event.objects.get(event_id=event_id)
        if event.time > timezone.now():
            EventSignup.objects.filter(user=user, event_id=event_id).delete()
            messages.success(request, 'You have successfully canceled your signup for the event.')
        else:
            messages.error(request, 'You cannot cancel signup for past events.')
        return redirect('user_profile')

    return render(request, 'accounts/user_profile.html', {'user': user, 'events': events})

@login_required
def change_login_details(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_email = request.POST['email']
        new_password = request.POST['password']
        user = request.user

        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email
        if new_password:
            user.set_password(new_password)

        user.save()

        messages.success(request, 'Your login details have been updated successfully.')
        return redirect('user_profile')
    return render(request, 'accounts/user_profile.html')

@login_required
def delete_event(request, event_id):
    try:
        event = Event.objects.get(event_id=event_id, organizer=request.user)
        if event.time > timezone.now():
            event.delete()
            messages.success(request, 'Event deleted successfully!')
        else:
            messages.error(request, 'You cannot delete past events.')
    except Event.DoesNotExist:
        messages.error(request, 'Event not found or you do not have permission to delete it.')
    return redirect('event_manager_profile')

@login_required
def update_event(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        time = request.POST.get('time')
        event_type = request.POST.get('type')
        tags = request.POST.get('tags')

        try:
            event = Event.objects.get(event_id=event_id, organizer=request.user)
            if title:
                event.title = title
            if description:
                event.description = description
            if location:
                event.location = location
            if time:
                event.time = time
            if event_type:
                event.type = event_type
            if tags:
                event.tags = tags
            event.save()

            messages.success(request, 'Event updated successfully!')
        except Event.DoesNotExist:
            messages.error(request, 'Event not found or you do not have permission to update it.')

    return redirect('event_manager_profile')
