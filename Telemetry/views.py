from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json

@login_required
def home(request):
    
    r = requests.get('http://localhost:5001/init')
    json_sensors = json.dumps(r.text)
    return render(request, 'Telemetry/home.html', {'r':json_sensors})

