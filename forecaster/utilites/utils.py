import os
from datetime import datetime

import requests
from requests import HTTPError


def get_forecast():
    token = os.getenv('TOKEN', None)
    url = 'https://api.openweathermap.org/data/2.5/onecall'
    params = {
        'lat': '48.45',
        'lon': '34.98',
        'appid': token,
        'exclude': 'minutely,hourly',
        'units': 'metric'
    }
    responce = requests.get(url, params=params)
    try:
        responce.raise_for_status()
    except HTTPError as e:
        print(str(e))
    return responce.json()


def form_forecast():
    forecast = get_forecast()

    def _now(data):

        title = datetime.fromtimestamp(
            data['current']['dt']
             ).strftime("%I:%M:%S")

        temperature = str(data['current']['temp']) + ' C'
        wind = str(data['current']['wind_speed']) + ' m/s'
        weather = str(data['current']['weather'][0]['description'])

        return {
            'title': title,
            'names': ['temperature', 'wind', 'weather'],
            'values': [temperature, wind, weather]
        }

    def _day(data, i):

        title = (
            datetime.fromtimestamp(data['daily'][i]['dt'])
        ).strftime("%A, %B %d, %Y")

        t_min = str(data['daily'][i]['temp']['min'])
        t_max = str(data['daily'][i]['temp']['max'])
        temperature = t_max + ' / ' + t_min + ' C'
        wind = str(data['daily'][i]['wind_speed']) + ' m/s'
        weather = str(data['daily'][i]['weather'][0]['description'])

        return {
            'title': title,
            'names': ['temperature\nmax / min', 'wind', 'weather'],
            'values': [temperature, wind, weather]
        }

    return {
        'now': _now(forecast),
        'today': _day(forecast, 0),
        'tomorrow': _day(forecast, 1)
    }
