from kivy.app import App
from kivy.base import ExceptionHandler, ExceptionManager
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from forecaster.config import PLUG_DATA
from forecaster.graphic.screen import MainScreen
from forecaster.utilites.utils import form_forecasts


class ForecasterApp(App):
    plug_data = PLUG_DATA

    def __init__(self, **kwargs):
        super(ForecasterApp, self).__init__(**kwargs)
        self.main_screen = MainScreen(self.plug_data)

    def build(self):
        return self.main_screen

    def on_start(self):
        self.main_screen.update_text(form_forecasts())


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
