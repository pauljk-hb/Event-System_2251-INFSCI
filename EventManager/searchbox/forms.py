from django import forms

class EventSearchForm(forms.Form):
    location = forms.CharField(required=False, label="Location")
    start_time = forms.DateTimeField(
        required=False,
        label="Start Time",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    end_time = forms.DateTimeField(
        required=False,
        label="End Time",
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    event_type = forms.CharField(required=False, label="Event Type")
