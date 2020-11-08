from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from forecaster.utils import form_forecast


Window.size = (500, 880)


class StringBox(BoxLayout):
    """Form string for 3 cells"""

    def __init__(self, text: list, **kwargs):
        super(StringBox, self).__init__(**kwargs)
        self.text = text
        self.add_widget(Label(text=self.text[0]))
        self.add_widget(Label(text=self.text[1]))
        self.add_widget(Label(text=self.text[2]))


class DataGroup(BoxLayout):
    """
    Form group widgets:
    =======title=======
    ==name==name==name=
    =value=value=value=

    """

    def __init__(self, data, **kwargs):
        super(DataGroup, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text=data['title']))
        self.add_widget(StringBox(data['names']))
        self.add_widget(StringBox(data['values']))


class MainScreen(BoxLayout):

    def __init__(self, data, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(DataGroup(data['now']))
        self.add_widget(DataGroup(data['today']))
        self.add_widget(DataGroup(data['tomorrow']))


class ForecasterApp(App):

    def build(self):
        return MainScreen(form_forecast())


if __name__ == '__main__':
    ForecasterApp().run()
