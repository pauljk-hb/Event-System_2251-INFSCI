from django.shortcuts import render

def event_search(request):
  # Retrieve the search query from the GET parameters
  query = request.GET.get("search", "")


  # Here you would typically query the database. For now, let's use a hardcoded list of events.
  events = [
      {"name": "Chess", "location": "Room 301", "tags":'chess, board game'},
      {"name": "Uno", "location": "Room 502", "tags": 'uno, card'},
  ]

  # Filter events based on the search query
  filtered_events = [event for event in events if query.lower() in event["tags"].lower()]


  # Pass filtered events to the template
  return render(request, "searchbox/event_search.html", {"events": filtered_events})


