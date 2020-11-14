from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


Window.size = (500, 880)


class StringBox(BoxLayout):
    """
    Widget, consisted form 3 cells per row:
    | cell_1 | cell_2 | cell_3 |
    """

    def __init__(self, content: list, **kwargs):
        super(StringBox, self).__init__(**kwargs)

        self.cell_1 = Label(text=content[0])
        self.cell_2 = Label(text=content[1])
        self.cell_3 = Label(text=content[2])

        self.add_widget(self.cell_1)
        self.add_widget(self.cell_2)
        self.add_widget(self.cell_3)

    def update_content(self, content):
        self.cell_1.text = content[0]
        self.cell_2.text = content[1]
        self.cell_3.text = content[2]


class ForecastWidget(BoxLayout):
    """
    Widget for viewing day forecast.
    main_title - date of forecast

    |      date_title       |
    | title | title | title |
    | value | value | value |

    """

    def __init__(self, day_forecast, **kwargs):
        super(ForecastWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.main_title = Label(text=day_forecast['date_title'])
        self.names = StringBox(day_forecast['titles'])
        self.values = StringBox(day_forecast['values'])

        self.add_widget(self.main_title)
        self.add_widget(self.names)
        self.add_widget(self.values)

    def update_forecast(self, day_forecast):
        self.main_title.text = day_forecast['date_title']
        self.names.update_content(day_forecast['titles'])
        self.values.update_content(day_forecast['values'])


class MainScreen(BoxLayout):

    def __init__(self, forecast, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.weather_now = ForecastWidget(forecast['now'])
        self.weather_today = ForecastWidget(forecast['today'])
        self.weather_tomorrow = ForecastWidget(forecast['tomorrow'])

        self.add_widget(self.weather_now)
        self.add_widget(self.weather_today)
        self.add_widget(self.weather_tomorrow)

    def update_text(self, data):
        self.weather_now.update_forecast(data['now'])
        self.weather_today.update_forecast(data['today'])
        self.weather_tomorrow.update_forecast(data['tomorrow'])
