from kivy.app import App
from kivy.base import ExceptionHandler, ExceptionManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from forecaster.graphic.screen import MainScreen
from forecaster.utilites.utils import form_forecast


class ForecasterApp(App):
    plug_data = {
        'now': {
            'title': '0',
            'names': ['0', '0', '0'],
            'values': ['0', '0', '0']
        },
        'today': {
            'title': '0',
            'names': ['0', '0', '0'],
            'values': ['0', '0', '0']
        },
        'tomorrow': {
            'title': '0',
            'names': ['0', '0', '0'],
            'values': ['0', '0', '0']
        },
    }

    def build(self):
        data = form_forecast()
        return MainScreen(data)


class Error(Exception, ExceptionHandler):

    def handle_exception(self, exception):
        Popup(
            title='OOPS',
            content=(Label(text=str(exception))),
            size_hint=(None, None),
            size=(200, 200)
        ).open()
        return ExceptionManager.PASS


ExceptionManager.add_handler(Error())


if __name__ == '__main__':
    ForecasterApp().run()
