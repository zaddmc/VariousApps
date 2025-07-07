from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput


class CardCounter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.players = [PlayerStruct(name) for name in ["David", "Far", "Jonas"]]

        self.player_grid = GridLayout(cols=len(self.players))
        for player in self.players:
            self.player_grid.add_widget(
                Label(
                    text=player.name,
                    height=20,
                    size_hint_max_y=24,
                )
            )
        for player in self.players:
            self.player_grid.add_widget(
                Label(text=player.score, height=20, size_hint_max_y=24)
            )
        self.add_widget(self.player_grid)
        self.add_input_row(None)
        self.add_input_row(None)
        self.add_input_row(None)
        self.add_input_row(None)
        self.add_input_row(None)

        # Handle Data, this was a test and can be removed
        data_grid = GridLayout(cols=2, spacing=5, padding=10)
        data_grid.add_widget(
            Button(
                text="Save", on_press=self.save_data, background_color=[1, 0.65, 0, 1]
            )
        )
        data_grid.add_widget(
            Button(
                text="Load", on_press=self.load_data, background_color=[1, 0.65, 0, 1]
            )
        )
        # self.add_widget(data_grid)

    def add_input_row(self, instance):
        for player in self.players:
            self.player_grid.add_widget(
                TextInput(
                    text="",
                    size_hint_max_y=32,
                    halign="center",
                    multiline=False,
                    ids={"name": player.name, "obj": player},
                    on_text_validate=self.data_input,
                )
            )

    def data_input(self, instance):
        num = instance.text
        if not num.isdigit():
            print("Not a number")
            return
        num = int(num)
        if num % 5 != 0:
            print("Not a valid number (Not divisible by 5)")
            return

        player = self.players[self.players.index(instance.ids["obj"])]
        player.score = str(int(player.score) + num)

        self.player_grid.children[-len(self.players) - 1 : len(self.players) - 1 : -1][
            self.players.index(player)
        ].text = player.score

    def save_data(self, instance):
        with open("mydata.txt", "w") as file:
            file.write(self.result.text)

    def load_data(self, instance):
        try:
            with open("mydata.txt", "r+") as file:
                self.result.text = file.read()
        except FileNotFoundError:
            print("File not found")
            return


class PlayerStruct:
    def __init__(self, name):
        self.name = name
        self.score = "0"


class CardCounterApp(App):
    def build(self):
        return CardCounter()


if __name__ == "__main__":
    CardCounterApp().run()
