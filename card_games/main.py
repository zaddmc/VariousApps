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
            background_color=[0.2, 0.2, 0.2, 1],
            foreground_color=[1, 1, 1, 1],
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
                button = Button(
                    text=item,
                    font_size=32,
                    on_press=self.button_clicked,
                    background_color=self.set_button_color(item),
                )
                grid.add_widget(button)
        self.add_widget(grid)

    def set_button_color(self, label):
        if label in {"C", "+/-", "%"}:
            return [0.6, 0.6, 0.6, 1]
        if label in {"/", "*", "-", "+", "="}:
            return [1, 0.65, 0, 1]
        return [0.3, 0.3, 0.3, 1]

    def button_clicked(self, instance):
        text = instance.text
        operators = [".", "/", "*", "-", "+"]

        print(self.result.text)
        if text == "ERROR!":
            self.result.text = ""

        match text:
            case "C":
                self.result.text = ""
            case "+/-":
                self.toggle_negative()
            case "%":
                self.result.text += "Why?"
            case "=":
                self.calculate()
            case num if num.isdigit():
                self.result.text += num
            case opt if opt in operators:
                if not self.result.text[-1] in operators:
                    self.result.text += text
            case _:
                print("Unrecognized button Pressed")
                # print(" " * 11, f'case "{text}":', "\n", " " * 15, "pass")

    def calculate(self):
        try:
            self.result.text = str(eval(self.result.text))
        except Exception:
            self.result.text = "ERROR!"

    def toggle_negative(self):
        if not self.result.text:
            print("Invalid text")

        if self.result.text[0] == "-":
            self.result.text = self.result.text[1:]
        else:
            self.result.text = "-" + self.result.text


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
