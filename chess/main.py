from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

Window.size = (800, 800)


class Chess(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        grid = GridLayout(cols=8, rows=8, spacing=5, padding=10)
        for x in range(8):
            for y in range(8):
                grid.add_widget(Tile([0, 0, 0, 1] if x % 2 == 0 else [1, 1, 1, 1]))
        self.add_widget(grid)

    def set_tile_color(self, label):
        return [0.3, 0.3, 0.3, 1]

    def button_clicked(self, instance):
        text = instance.text


class Tile(Widget):
    def __init__(self, rgba, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(*rgba)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ChessApp(App):
    def build(self):
        return Chess()


if __name__ == "__main__":
    ChessApp().run()
