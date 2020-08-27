from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests

@login_required
def home(request):
    
    r = requests.get('http://localhost:5001/init')
    print(r.text)
    return render(request, 'Telemetry/home.html', {'r':r.text})

