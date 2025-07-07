from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class CardCounter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.result = TextInput(
            size_hint_y=0.2,
            halign="right",
            background_color=[0.2, 0.2, 0.2, 1],
            foreground_color=[1, 1, 1, 1],
        )
        self.add_widget(self.result)

        grid = GridLayout(cols=2, spacing=5, padding=10)
        grid.add_widget(
            Button(
                text="Save", on_press=self.save_data, background_color=[1, 0.65, 0, 1]
            )
        )
        grid.add_widget(
            Button(
                text="Load", on_press=self.load_data, background_color=[1, 0.65, 0, 1]
            )
        )
        self.add_widget(grid)

    def save_data(self, instance):
        with open("mydata.txt", "w") as file:
            file.write(self.result.text)

    def load_data(self, instance):
        with open("mydata.txt", "r") as file:
            self.result.text = file.read()


class CardCounterApp(App):
    def build(self):
        return CardCounter()


if __name__ == "__main__":
    CardCounterApp().run()
