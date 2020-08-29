from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json

@login_required
def home(request):
    
    r = requests.get('http://localhost:5001/init')
    json_sensors = json.dumps(r.text)
    data = r.json()
    test_dict = {
        "sensor": data
    }
   # print(data[0].lower())
    list_sensors = []
    def sensor_list():
        for sensor in data:
            s_name = requests.get("http://localhost:5001/sensors/?sensor=" + sensor + "&number=1")
            data_sensor = s_name.json()
            list_sensors.append(data_sensor[0])
    sensor_list()
    sensor_names = requests.get("http://localhost:5001/sensors/?sensor=bat_volts&number=1")
    names_list = sensor_names.json()
    print("names_list", names_list)
    names = names_list[0]['name']

    return render(request, 
                'Telemetry/home.html', 
                {'r':json_sensors, 
                'n': test_dict['sensor'], 
                'sensors': list_sensors})

