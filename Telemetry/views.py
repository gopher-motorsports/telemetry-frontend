from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json

@login_required
def home(request):
    num_cols = 5
    r = requests.get('http://localhost:5001/init')
    json_sensors = json.dumps(r.text)
    data = r.json()
    
    list_sensors = []
    def sensor_list():
        for sensor in data:
            s_name = requests.get("http://localhost:5001/sensors/?sensor=" + sensor + "&number=1")
            data_sensor = s_name.json()
            
            data_sensor[0]['sensor'] = sensor
            list_sensors.append(data_sensor[0])
    sensor_list()
    return render(request, 
                'Telemetry/home.html', 
                {
                'sensors': list_sensors,
                'cols': num_cols,
                'cols_list': range(num_cols)}
                )

