from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.utils import rgba


class Backend(GridLayout):
    def __init__(self, grid_size: int, **kwargs):
        super().__init__(**kwargs)
        self.cols = grid_size
        self.rows = grid_size
        self.spacing = 20

        self.grid_size = grid_size

        for _ in range(grid_size * grid_size):
            self.add_widget(Tile("2048"))

    def add_random(self):
        self.add_widget(Tile())
        self.add_widget(Tile())


class Tile(Button):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.background_color = rgba("#555555")
        self.text = value
        self.bind(font_size=self.resize, size=self.resize)

    def resize(self, *args):
        self.font_size = self.width / 3
