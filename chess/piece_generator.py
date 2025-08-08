import importlib

from kivy.graphics import Color, Line
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.utils import rgba

from my_enums import Actions, PieceColor, PieceSpecies


class BoardGenerator:
    """There is some magic numbers, that assume a normal board and
    that the grid remains a 8x8"""

    def __init__(self):
        self.grid: GridLayout = GridLayout(cols=8, rows=8)

        self.__place_backline("b")
        self.__place_pawns("b")
        self.__place_blanks()
        self.__place_pawns("w")
        self.__place_backline("w")

    def get_board(self):
        return self.grid

    def __place_pawns(self, color: str):
        for _ in range(8):
            self.__placer(color + "_pawn")

    def __place_blanks(self):
        for _ in range(4):
            for _ in range(8):
                self.__placer("blank")

    def __place_backline(self, color: str):
        """Input 'color' is expected to be either 'w' or 'b'"""
        backline = [
            "rook",
            "knight",
            "bishop",
            "queen",
            "king",
            "bishop",
            "knight",
            "rook",
        ]

        for piece in backline:
            self.__placer(color + "_" + piece)

    def __placer(self, species: str):
        if species == "blank":
            self.grid.add_widget(Blank())
        else:
            source = "Images/" + species + ".png"
            self.grid.add_widget(Piece(source))


class BasePiece(ButtonBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outline = None

    def on_press(self):
        """This is function is cursed
        If i import normally, it will result in a circle
        due to 'MovementHandler' using 'Blank' which is a derivative of this
        To solve this issue, behavior is imported dynammically, which is cursed"""
        BasePiece.get_behavior().tile_clicked(self)

    behavior = None

    @staticmethod
    def get_behavior():
        """To avoid importing the module multiple times
        Making it statically dynammic"""
        if not BasePiece.behavior:
            module = importlib.import_module("piece_actions")
            BasePiece.behavior = getattr(module, "Behavior")

        return BasePiece.behavior

    def get_index(self) -> int:
        return self.parent.children.index(self)

    def get_sibling(self, sibling: int):
        """Get sibling by index"""
        return self.parent.children[sibling]

    def __str__(self):
        try:
            return f"{self.species} {self.piece_color} {self.get_index()}"
        except:
            return "BasePiece"

    def highligt_me(self, action: Actions = Actions.MOVE):
        match action:
            case Actions.MOVE:
                color = [0.196, 0.659, 0.322, 1]
            case Actions.ATTACK:
                color = [0.612, 0.055, 0.102, 1]
            case _:
                color = [0.267, 0.267, 0.267, 1]

        with self.canvas:
            Color(*color)
            self.outline = Line(
                rounded_rectangle=(
                    self.pos[0],
                    self.pos[1],
                    self.size[0],
                    self.size[1],
                    40,
                    40,
                    40,
                    40,
                ),
                width=5,
            )

    def remove_highlights(self):
        for piece in self.parent.children:
            if piece.outline:
                piece.canvas.remove(piece.outline)
                piece.outline = None


class Blank(BasePiece, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.species: PieceSpecies = PieceSpecies.BLANK
        self.piece_color: PieceColor = PieceColor.BLANK


class Piece(BasePiece, Image):
    def __init__(self, source: str, **kwargs):
        """Give the source to an image and it will auto detect
          which species and color the piece will be.
        Given the constraint that the source is formulated like 'Images/c_name.png'
          where c is one letter for either w for white and b for black
          and name is lower caps for the species of the wanted piece
          Note, It does not have to be 'Images/' it just needs that length"""
        super().__init__(**kwargs)

        self.piece_color: PieceColor = (
            PieceColor.BLACK if source[7] == "b" else PieceColor.WHITE
        )
        self.species: PieceSpecies = PieceSpecies(source[9:-4])
        self.source: str = source

        # Used for certain logic for movement
        self.moves: int = 0
