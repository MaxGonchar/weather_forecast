from datetime import datetime

import requests
from requests import HTTPError

from forecaster.config import PARAMS, URL


def get_forecasts():
    response = requests.get(URL, params=PARAMS)
    try:
        response.raise_for_status()
    except HTTPError as e:
        print(str(e))
    return response.json()


def form_forecasts():
    forecasts = get_forecasts()

    def _now(data):

        title = datetime.fromtimestamp(
            data['current']['dt']
             ).strftime("%I:%M:%S")

        temperature = str(data['current']['temp']) + ' C'
        wind = str(data['current']['wind_speed']) + ' m/s'
        weather = str(data['current']['weather'][0]['description'])

        return {
            'date_title': title,
            'titles': ['temperature', 'wind', 'weather'],
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
            'date_title': title,
            'titles': ['temperature\nmax / min', 'wind', 'weather'],
            'values': [temperature, wind, weather]
        }

    print('==formed==')
    return {
        'now': _now(forecasts),
        'today': _day(forecasts, 0),
        'tomorrow': _day(forecasts, 1)
    }
