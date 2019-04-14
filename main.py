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

    def calculate(self):
        try:
            self.formula = str(eval(self.label.text))
        except ZeroDivisionError:
            self.formula="opening a black hole"
            # TODO: open a black hole here
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

        # some crutch here
        self.label = Label(text='0', font_size=40, halign='right', text_size=(295, 100), size_hint=(1, 0.4))

        self.formula = '0'
        box_layout = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(rows=5, cols=4)
        box_layout.add_widget(self.label)

        # magic

        for i in self.operations:
            if not bool(self.operations[i]): # if there is no value in dictionary this will be False(cause of not it will be True)
                grid_layout.add_widget(Button(text=f"{i}",on_press=self.add_a_thing))
            else:
                grid_layout.add_widget(Button(text=f"{i}",on_press=self.operations[i]))

        box_layout.add_widget(grid_layout)
        return box_layout

    operations ={
                '%':'',
                '/':'',
                '*':'',
                '-':'',
                '7':'',
                '8':'',
                '9':'',
                '+':'',
                '4':'',
                '5':'',
                '6':'',
                'Clr':clear_label,
                '1':'',
                '2':'',
                '3':'',
                '=':calculate,
                '':'',
                '0':'',
                '.':'',
                '':'',
                }

if __name__ == "__main__":
    MyApp().run()
