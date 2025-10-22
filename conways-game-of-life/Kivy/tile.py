from copy import deepcopy

from kivy.graphics import Color, Rectangle
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.utils import rgba


class Tile(Button):
    Color_Alive = rgba("#f2e1c3")
    Color_Dead = rgba("#c3a082")

    def __init__(self, idx, idy, **kwargs):
        super().__init__(**kwargs)

        self.is_alive = False
        color = Tile.Color_Alive if self.is_alive else Tile.Color_Dead

        with self.canvas:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_press(self):
        self.switch()

    def switch(self, to_state: bool = None):
        if to_state == None:
            self.is_alive = not self.is_alive
        else:
            self.is_alive = to_state

        color = Tile.Color_Alive if self.is_alive else Tile.Color_Dead
        with self.canvas:
            Color(*color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    @staticmethod
    def count_neighbors(cells, idx, idy):
        neighbors = []
        rows, cols = len(cells), len(cells[0])

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # skip the center cell itself
                nx, ny = idx + dx, idy + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    neighbors.append(cells[nx][ny])
        return neighbors.count(True)

    @staticmethod
    def step_cells(grid):
        new_cells = grid.children
        for idx in range(grid.rows):
            for idy in range(grid.cols):
                alive_neigh = Tile.count_neighbors(cells, idx, idy)
                if val and alive_neigh < 2:
                    new_state = False
                elif val and alive_neigh in [2, 3]:
                    new_state = True
                elif val and alive_neigh > 3:
                    new_state = False
                elif not val and alive_neigh == 3:
                    new_state = True

        return new_cells

    @staticmethod
    def make_grid(grid_size):
        grid = GridLayout(cols=grid_size, rows=grid_size)

        for idx in range(grid_size):
            for idy in range(grid_size):
                tile = Tile(idx, idy)
                grid.add_widget(tile)
        return grid
