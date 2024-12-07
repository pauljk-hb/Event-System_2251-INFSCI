
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from events.models import EventSignup

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

    return render(request, 'accounts/event_manager_profile.html')

# Profile page for standard users
# Only accessible to users with is_event_manager = False
@login_required
def user_profile(request):
    user = request.user
    signups = EventSignup.objects.filter(user=user).select_related('event')
    events = [signup.event for signup in signups]
    return render(request, 'accounts/user_profile.html', {'user': user, 'events': events})

