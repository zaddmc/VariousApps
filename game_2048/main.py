from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

from backend import Backend

Window.size = (800, 800)


class G2048(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.backend = Backend(4)
        self.add_widget(self.backend)


class G2048App(App):
    def build(self):
        return G2048()


if __name__ == "__main__":
    G2048App().run()
