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

        self.add_widget(Tile.make_grid())

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

    @staticmethod
    def make_grid(grid_size: int = 8):
        grid = GridLayout(cols=grid_size, rows=grid_size)
        my_switch: bool = False
        for _ in range(grid_size):
            for _ in range(grid_size):
                color = [0, 0, 0, 1] if my_switch else [1, 1, 1, 1]
                my_switch = not my_switch
                tile = Tile(color)
                grid.add_widget(tile)
            if grid_size % 2 == 0:
                my_switch = not my_switch
        return grid


class ChessApp(App):
    def build(self):
        return Chess()


if __name__ == "__main__":
    ChessApp().run()
