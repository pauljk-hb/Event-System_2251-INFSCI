from django.shortcuts import render

def event_search(request):
    # Retrieve the search query from the GET parameters
    query = request.GET.get("search", "")

    # Here you would typically query the database. For now, let's use a hardcoded list of events.
    events = [
        {"name": "Chess", "location": "Room 301"},
        {"name": "Uno", "location": "Room 502"},
    ]
    
    
    # Filter events based on the search query
    filtered_events = [event for event in events if query.lower() in event["name"].lower()]

    # Pass filtered events to the template
    return render(request, "searchbox/event_search.html", {"events": filtered_events})

