import time

from kivy.app import App
from kivy.uix.button import Button

from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'height', 400)
Config.set('graphics', 'width', 300)


class MyApp(App):

    def calculate(self, instance):

        try:
            self.formula = str(eval(self.label.text))
        except ZeroDivisionError:
            self.formula="ошибка"
        self.update_label()
    def clear_label(self, instance):
        self.formula = '0'
        self.update_label()

    def update_label(self):
        self.label.text = self.formula

    def add_a_thing(self, instance):
        if self.formula == "0":
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def build(self):

        self.label = Label(text='0', font_size=40, halign='right', text_size=(295, 100), size_hint=(1, 0.4))

        self.formula = '0'
        box_layout = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(rows=5, cols=4)
        box_layout.add_widget(self.label)

        grid_layout.add_widget(Button(text='%', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='/', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='*', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='-', on_press=self.add_a_thing))

        grid_layout.add_widget(Button(text='7', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='8', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='9', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='+', on_press=self.add_a_thing))

        grid_layout.add_widget(Button(text='4', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='5', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='6', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='Clr', on_press=self.clear_label))

        grid_layout.add_widget(Button(text='1', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='2', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='3', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='=', on_press=self.calculate))


        grid_layout.add_widget(Button(text=''))
        grid_layout.add_widget(Button(text='0', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text='.', on_press=self.add_a_thing))
        grid_layout.add_widget(Button(text=''))

        box_layout.add_widget(grid_layout)
        return box_layout


if __name__ == "__main__":
    MyApp().run()
