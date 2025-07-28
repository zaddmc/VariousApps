from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.utils import rgba

from piece_generator import BoardGenerator

Window.size = (800, 800)


class Chess(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.surface_grid = Tile.make_grid()
        self.add_widget(self.surface_grid)

        board_generator = BoardGenerator()
        self.piece_grid = board_generator.get_board()
        self.add_widget(self.piece_grid)

    def piece_clicked(self, instance):
        text = instance.text
        print("I am a button")


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
                color = rgba("#c3a082") if my_switch else rgba("#f2e1c3")
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
