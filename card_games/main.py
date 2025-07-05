from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Window.size = (300, 500)


class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.result = TextInput(
            font_size=45,
            size_hint_y=0.2,
            readonly=True,
            halign="right",
            multiline=False,
        )
        self.add_widget(self.result)

        buttons = [
            ["C", "+/-", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", "00", ".", "="],
        ]

        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in buttons:
            for item in row:
                button = Button(text=item, font_size=32, on_press=self.button_clicked)
                grid.add_widget(button)
        self.add_widget(grid)

    def button_clicked(self, instance):
        text = instance.text

        match text:
            case "C":
                pass
            case "+/-":
                pass
            case "0":
                pass
            case "00":
                pass
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case ".":
                pass
            case "/":
                pass
            case "*":
                pass
            case "-":
                pass
            case "+":
                pass
            case "=":
                pass
            case "%":
                pass
            case _:
                print("Unrecognized button Pressed")
                # print(" " * 11, f'case "{text}":', "\n", " " * 15, "pass")


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
