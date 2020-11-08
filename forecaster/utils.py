from datetime import datetime, timedelta

import requests


def get_forecast():
    url = 'https://api.openweathermap.org/data/2.5/onecall'
    params = {
        'lat': '48.45',
        'lon': '34.98',
        'appid': '9f554879d5da54b5af8d93265adc60d0',
        'exclude': 'minutely,hourly',
        'units': 'metric'
    }
    responce = requests.get(url, params=params)
    return responce.json()


def form_forecast():
    data = get_forecast()

    now = datetime.fromtimestamp(data['current']['dt']).strftime("%I:%M:%S")
    today = datetime.fromtimestamp(data['current']['dt']).strftime("%A, %B %d, %Y")
    tomorrow = (
        datetime.fromtimestamp(data['current']['dt']) + timedelta(1)
    ).strftime("%A, %B %d, %Y")

    now_temperature = str(data['current']['temp']) + ' C'
    now_wind = str(data['current']['wind_speed']) + ' m/s'
    now_weather = str(data['current']['weather'][0]['description'])

    today_temperature = (str(data['daily'][0]['temp']['max']) + ' / ' + str(data['daily'][0]['temp']['min']) + ' C')
    today_wind = str(data['daily'][0]['wind_speed']) + ' m/s'
    today_weather = str(data['daily'][0]['weather'][0]['description'])

    tomorrow_temperature = (str(data['daily'][1]['temp']['max']) + ' / ' + str(data['daily'][0]['temp']['min']) + ' C')
    tomorrow_wind = str(data['daily'][1]['wind_speed']) + ' m/s'
    tomorrow_weather = str(data['daily'][1]['weather'][0]['description'])


    return {
        'now': {
            'title': now,
            'names': ['temperature', 'wind', 'weather'],
            'values': [now_temperature, now_wind, now_weather]
        },
        'today': {
            'title': today,
            'names': ['temperature\nmax / min', 'wind', 'weather'],
            'values': [today_temperature, today_wind, today_weather]
        },
        'tomorrow': {
            'title': tomorrow,
            'names': ['temperature\nmax / min', 'wind', 'weather'],
            'values': [tomorrow_temperature, tomorrow_wind, tomorrow_weather]
        }
    }
