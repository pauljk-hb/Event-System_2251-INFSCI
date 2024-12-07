from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def events(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'events/events.html', context)

def event_detail(request, event_id):
    # Hole das Event anhand der ID oder zeige 404-Seite
    event = get_object_or_404(Event, event_id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})
