from django.shortcuts import render
from .forms import EventRegistrationForm


def register_event(req):
    success = False
    if req.method == 'POST':
        form = EventRegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            form = EventRegistrationForm()
            success = True
    else:
        form = EventRegistrationForm()
    return render(req, 'register.html', {'form': form, 'success': success})
