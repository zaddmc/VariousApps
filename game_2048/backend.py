import random

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
            self.add_widget(Tile(""))

        self.add_random()
        self.add_random()

    def add_random(self):

        try:
            index_to_change = random.choice(list(self.get_free_tiles()))
        except IndexError:
            raise Exception("Game Over, poor loser")

        self.remove_widget(self.children[index_to_change])
        self.add_widget(Tile("2"), index_to_change)

    def get_free_tiles(self):
        for child in self.children:
            if child.text == "":
                yield child.get_index()

    def take_input(self, value: str):
        match value:
            case "right":
                pass
            case "left":
                pass
            case "up":
                pass
            case "down":
                self.move_tiles("down")
            case _:
                raise ValueError(f"Unexpected: {value}")

        self.add_random()

    def move_tiles(self, direction):
        print(self.get_items(direction))

    def get_items(self, direction):
        lst = self.children
        return [
            lst[i * self.grid_size : (i + 1) * self.grid_size]
            for i in range(self.grid_size)
        ]


class Tile(Button):
    def __init__(self, value, **kwargs):
        super().__init__(**kwargs)
        self.background_color = rgba("#555555")
        self.text = value
        self.bind(size=self.resize)

    def resize(self, *args):
        self.font_size = self.width / 3

    def get_index(self):
        return self.parent.children.index(self)
