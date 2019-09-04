from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.

def jam_session(request, jam_session_name):
    return render(request, 'jamsession/jam_session.html', {
        'session_name_json': mark_safe(json.dumps(jam_session_name))
    })
