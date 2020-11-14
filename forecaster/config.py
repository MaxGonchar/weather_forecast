import os


TOKEN = os.getenv('TOKEN', None)
URL = 'https://api.openweathermap.org/data/2.5/onecall'

PARAMS = {
        'lat': '48.45',
        'lon': '34.98',
        'appid': TOKEN,
        'exclude': 'minutely,hourly',
        'units': 'metric'
    }

PLUG_DATA = {
        'now': {
            'date_title': '0',
            'titles': ['0', '0', '0'],
            'values': ['0', '0', '0']
        },
        'today': {
            'date_title': '0',
            'titles': ['0', '0', '0'],
            'values': ['0', '0', '0']
        },
        'tomorrow': {
            'date_title': '0',
            'titles': ['0', '0', '0'],
            'values': ['0', '0', '0']
        },
    }