from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Event, EventSignup
from django.utils.timezone import now
from datetime import datetime, timedelta

def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

def events(request):
    all_events = Event.objects.all()

    all_events = all_events.filter(time__gt=now())

    tags = set()
    for event in all_events:
        tags.update(event.tags.split(','))

    tag_filter = request.GET.get('tag')
    if tag_filter:
        all_events = all_events.filter(tags__icontains=tag_filter)

    sort_by = request.GET.get('sort_by', 'time')
    if sort_by == 'title':
        all_events = all_events.order_by('title')
    elif sort_by == 'type':
        all_events = all_events.order_by('type')
    else:
        all_events = all_events.order_by('time')

    for event in all_events:
        event.split_tags = event.tags.split(',')
    return render(request, 'events/events.html', {'events': all_events, 'tags': tags, 'selected_tag': tag_filter})

def event_detail(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    event.split_tags = event.tags.split(',')
    signup_count = EventSignup.objects.filter(event=event).count()

    if request.method == 'POST':
        if request.user.is_authenticated:
            if event.time <= now():
                messages.error(request, "You cannot register for past or ongoing events.")
                return HttpResponseRedirect(reverse('event_detail', args=[event_id]))

            if EventSignup.objects.filter(user=request.user, event=event).exists():
                messages.warning(request, "You are already registered for this event.")
            else:
                EventSignup.objects.create(user=request.user, event=event)
                messages.success(request, "Successfully registered for the event!")
            return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
        else:
            messages.error(request, "You need to log in to register for an event.")
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'events/event_detail.html', {'event': event, 'signup_count': signup_count})

def history_events(request):
    events = Event.objects.filter(time__lt=now())
    events = events.order_by('-time')
    return render(request, 'events/history_events.html', {'events': events})

def download_event_ics(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    end_time = (event.time + timedelta(hours=1)).strftime('%Y%m%dT%H%M%S')
    start_time = event.time.strftime('%Y%m%dT%H%M%S')
    end_time = (event.time + timedelta(hours=1)).strftime('%Y%m%dT%H%M%S')
    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Your Organization//Your App//EN
BEGIN:VEVENT
UID:{event_id}@yourapp.com
DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%S')}
DTSTART;TZID=Europe/Berlin:{start_time}
DTEND;TZID=Europe/Berlin:{end_time}
SUMMARY:{event.title}
DESCRIPTION:{event.description}
LOCATION:{event.location}
END:VEVENT
END:VCALENDAR
        """

    response = HttpResponse(ics_content, content_type="text/calendar")
    response['Content-Disposition'] = f'attachment; filename="{event.title}.ics"'
    return response
