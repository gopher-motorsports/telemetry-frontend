from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests

@login_required
def home(request):
    
    r = requests.get('http://localhost:5001/init')
    print(r.text)
    n = r.text.split(',')
    n[0] = n[0][1:]
    n[-1] = n[-1][:-1]
    return render(request, 'Telemetry/home.html', {'r':n})

