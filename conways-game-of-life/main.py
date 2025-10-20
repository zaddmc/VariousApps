from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Window.size = (1000, 800)

from tile import Tile


class ConwayGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="horizontal", **kwargs)
        self.grid_size_def = 20
        self.grid_size = self.grid_size_def

        # Options in making
        self.options = BoxLayout(orientation="vertical", size_hint_x=0.2)

        def size_on_enter(instance):
            value = instance.text
            if value.isdigit():
                self.grid_size = int(value)
            else:
                self.grid_size = self.grid_size_def
            self.remove_widget(self.grid)
            self.grid = Tile.make_grid(self.grid_size)
            self.add_widget(self.grid)

        set_grid_size = TextInput(text="20", multiline=False)
        set_grid_size.bind(on_text_validate=size_on_enter)
        self.options.add_widget(set_grid_size)

        def step_on_press(instance):
            old_cells = Tile.Cells
            new_cells = Tile.step_cells(old_cells)
            self.remove_widget(self.grid)
            self.grid = Tile.make_grid(self.grid_size, new_cells)
            self.add_widget(self.grid)

        step_button = Button(text="Step one evolution")
        step_button.bind(on_press=step_on_press)
        self.options.add_widget(step_button)

        self.add_widget(self.options)

        self.grid = Tile.make_grid(self.grid_size)
        self.add_widget(self.grid)


class ConwayGameApp(App):
    def build(self):
        return ConwayGame()


if __name__ == "__main__":
    ConwayGameApp().run()
