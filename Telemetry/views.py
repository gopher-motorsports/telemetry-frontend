from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
import json

@login_required
def home(request):
    #The number of horizontal columns on the page
    num_cols = 5
    #Gets a list of the sensor names
    r = requests.get('http://localhost:5001/init')
    json_sensors = json.dumps(r.text)
    #Converts that list to a JSON object that we can work with
    data = r.json()
    list_sensors = []
    #This function takes each sensor in 'data' and gets the attributes of that sensor.
    #It changes 'list_sensors' into an array with a dictionary of all the sensor's information
    def sensor_list():
        for sensor in data:
            #Gets each of the sensors in 'data'
            s_name = requests.get("http://localhost:5001/sensors/?sensor=" + sensor + "&number=1")
            #Converts all that to a JSON dictionary we can use
            data_sensor = s_name.json()
            #Adds a key 'sensor' to the dictionary that stores the sensor's computer readable name
            data_sensor[0]['sensor'] = sensor
            #Adds this dictionary to the list 'list_sensors'
            list_sensors.append(data_sensor[0])
    #Actually runs the functions so the above can happen
    sensor_list()
    #Passes these values into the 'home.html' template
    return render(request, 
                'Telemetry/home.html', 
                {
                'sensors': list_sensors,
                'cols': num_cols,
                #Not really a list. This is needed to iterate in the 'home.html' template
                'cols_list': range(num_cols)}
                )

