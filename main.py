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
    calculation_result = None
    def calculate(self,instance):
        try:
            self.calculation_result = eval(self.label_down.text)
            self.formula = str(self.calculation_result)
        except ZeroDivisionError:
            self.formula="ошибка"
        self.update_label_down()

    def clear_label_down(self, instance):
        self.formula = '0'
        self.update_label_down()

    def update_label_down(self):
        self.label_down.text = self.formula

    def update_label_top(self):
        self.label_top.text = str(self.calculation_result)
        self.formula = ""
        self.update_label_down()

    def add_a_thing(self, instance):
        if self.formula == "0":
            self.formula = ""
        if (instance.text in self.operators) and not (self.formula is "") and (self.formula[-1] in self.operators):

            self.update_label_down()
            return
        if self.formula == str(self.calculation_result):
            self.update_label_top()
        self.formula += str(instance.text)
        self.update_label_down()

    def build(self):
        self.label_top = Label(text='', font_size=40, halign='right', text_size=(295, 50), size_hint=(1, 0.2))
        self.label_down = Label(text='0', font_size=40, halign='right', text_size=(295, 50), size_hint=(1, 0.2))


        box_layout = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(rows=5, cols=4)
        box_layout.add_widget(self.label_top)
        box_layout.add_widget(self.label_down)


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
        grid_layout.add_widget(Button(text='Clr', on_press=self.clear_label_down))

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
    operators = "+-/%*"
    formula = '0'
if __name__ == "__main__":
    MyApp().run()