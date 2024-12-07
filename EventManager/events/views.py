from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Event, EventSignup
from django.utils.timezone import now

def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def events(request):
    all_events = Event.objects.all()
    for event in all_events:
        event.split_tags = event.tags.split(',')
    return render(request, 'events/events.html', {'events': all_events})

def event_detail(request, event_id):
    # Hole das Event anhand der ID oder zeige 404-Seite
    event = get_object_or_404(Event, event_id=event_id)
    event.split_tags = event.tags.split(',')

    if request.method == 'POST':
        if request.user.is_authenticated:
            # Überprüfen, ob das Event in der Zukunft liegt
            if event.time <= now():
                messages.error(request, "You cannot register for past or ongoing events.")
                return HttpResponseRedirect(reverse('event_detail', args=[event_id]))

            # Überprüfen, ob der Nutzer bereits registriert ist
            if EventSignup.objects.filter(user=request.user, event=event).exists():
                messages.warning(request, "You are already registered for this event.")
            else:
                EventSignup.objects.create(user=request.user, event=event)
                messages.success(request, "Successfully registered for the event!")
            return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
        else:
            messages.error(request, "You need to log in to register for an event.")
            return HttpResponseRedirect(reverse('login'))
    

    return render(request, 'events/event_detail.html', {'event': event})
