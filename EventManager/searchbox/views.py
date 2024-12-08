from django.shortcuts import render
from events.models import Event
from django.utils.timezone import now
from django.db.models import Q

def event_search(request):
    # Retrieve the search query from the GET parameters
    query = request.GET.get("search", "").lower()

    # If no search query is provided, return an empty list
    if not query:
        return render(request, "searchbox/event_search.html", {"events": [], "query": query})

    # Retrieve all events that are in the future and order them by time
    events = Event.objects.filter(time__gt=now()).order_by('time')

    # Filter events based on the search query
    events = events.filter(
        Q(title__icontains=query) |
        Q(location__icontains=query) |
        Q(tags__icontains=query)
    )

    # Pass filtered events to the template
    return render(request, "searchbox/event_search.html", {"events": events, "query": query})


