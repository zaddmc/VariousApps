from kivy.app import App
from kivy.core.window import Keyboard, Window
from kivy.uix.floatlayout import FloatLayout

from backend import Backend

Window.size = (800, 800)


class G2048(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.backend = Backend(4)
        self.add_widget(self.backend)

    def on_key_down(self, window, keycode, text, modifiers, is_repeat, *args):
        if keycode in [Keyboard.keycodes["right"], Keyboard.keycodes["d"]]:
            self.backend.take_input("right")
        if keycode in [Keyboard.keycodes["left"], Keyboard.keycodes["a"]]:
            self.backend.take_input("left")
        if keycode in [Keyboard.keycodes["up"], Keyboard.keycodes["w"]]:
            self.backend.take_input("up")
        if keycode in [Keyboard.keycodes["down"], Keyboard.keycodes["s"]]:
            self.backend.take_input("down")


class G2048App(App):
    def build(self):
        root = G2048()
        Window.bind(on_key_down=root.on_key_down)
        return root


if __name__ == "__main__":
    G2048App().run()
