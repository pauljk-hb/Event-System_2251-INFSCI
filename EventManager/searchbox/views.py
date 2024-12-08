from django.shortcuts import render
from events.models import Event

def event_search(request):
  # Retrieve the search query from the GET parameters
  query = request.GET.get("search", "").lower()

  # Retrieve all events
  events = Event.objects.all()

  # Filter events based on the search query
  filtered_events = []

  for event in events:
    if (query in event.title.lower() or 
        query in event.location.lower() or 
        query in event.tags.lower()):
      filtered_events.append(event)

  # Pass filtered events to the template
  return render(request, "searchbox/event_search.html", {"events": filtered_events, "query": query})


