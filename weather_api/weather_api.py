import flask
import requests
from datetime import datetime
import json
from flask import request
import os
from dotenv import load_dotenv

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/getWeather', methods =['GET'])
def getWeather():
    lattitude, longitude = return_long_lat(request)
    response = requests.get(buildString(lattitude, longitude, get_api_key()))
    json_list = response.json()
    new_json_str = '{}'
    new_json = json.loads(new_json_str)
    new_json.update({"date":datetime.utcfromtimestamp(json_list['daily'][0]['dt']).strftime('%Y-%m-%d')})
    new_json.update({"type":json_list['current']['weather'][0]['main']})
    new_json.update({"description":json_list['current']['weather'][0]['description']})
    new_json.update({"temperature":json_list['current']['temp']})
    new_json.update({"wind":{}})
    new_json['wind'] = {"speed":json_list['current']['wind_speed'],"bearing":json_list['current']['wind_deg']}
    new_json.update({"precip_prob":json_list['daily'][0]['pop'] * 100})
    new_json.update({"daily":[]})
    array = []
    for i in range(7):
        day_template = {"date":"DATE", "type":"TYPE", "description":"DESC", "temperature":{}}
        high_low = {"low":json_list['daily'][i]['temp']['min'], "high":json_list['daily'][i]['temp']['max']}
        day = day_template
        day['temperature'] = high_low
        day['date'] = datetime.utcfromtimestamp(json_list['daily'][i]['dt']).strftime('%Y-%m-%d')
        print("working on" + datetime.utcfromtimestamp(json_list['daily'][i]['dt']).strftime('%Y-%m-%d'))
        day['type'] = json_list['daily'][i]['weather'][0]['main']
        day['description'] = json_list['daily'][i]['weather'][0]['description']
        array.append(day)
        print("Here's the array's version:" + array[i]['date'])
        for x in array:
            val = array[i]['date']
    new_json['daily'] = array
    return flask.jsonify(new_json)

def return_long_lat(request):
    lattitude = request.args.get('latt', type=float)
    longitude = request.args.get('long', type=float)
    return lattitude, longitude

def ping():
    response = requests.get('https://api.openweathermap.org/data/2.5')
    return response.status_code

def buildString(lattitude, longitude, api_key):
    return ''.join(("https://api.openweathermap.org/data/2.5/onecall?lat=", str(lattitude), "&lon=", str(longitude), "&exclude=hourly,minutely,alerts&units=imperial&appid=", api_key))
 
def runApp():
    app.run(host='0.0.0.0')

def get_api_key():
    load_dotenv('../.env')
    return os.getenv('API_KEY')


if __name__ == '__main__':
    runApp()