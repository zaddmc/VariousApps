from enum import Enum

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class BoardGenerator:
    """There is some magic numbers, that assume a normal board and
    that the grid remains a 8x8"""

    def __init__(self):
        self.grid: GridLayout = GridLayout(cols=8, rows=8)

        self.place_backline("b")
        self.place_pawns("b")
        self.place_blanks()
        self.place_pawns("w")
        self.place_backline("w")

    def get_board(self):
        return self.grid

    def place_pawns(self, color: str):
        for _ in range(8):
            self.placer(color + "_pawn")

    def place_blanks(self):
        for _ in range(4):
            for _ in range(8):
                self.placer("blank")

    def place_backline(self, color: str):
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
            self.placer(color + "_" + piece)

    def placer(self, species: str):
        if species == "blank":
            self.grid.add_widget(Widget())
        else:
            source = "Images/" + species + ".png"
            self.grid.add_widget(Piece(source))


class Piece(ButtonBehavior, Image):
    def __init__(self, source: str, **kwargs):
        """Give the source to an image and it will auto detect
          which species and color the piece will be.
        Given the constraint that the source is formulated like 'Images/c_name.png'
          where c is one letter for either w for white and b for black
          and name is lower caps for the species of the wanted piece
          Note, It does not have to be 'Images/' it just needs that length"""
        super().__init__()

        self.piece_color: PieceColor = (
            PieceColor.BLACK if source[7] == "b" else PieceColor.WHITE
        )
        self.species: PieceSpecies = PieceSpecies(source[9:-4])
        self.source: str = source

        self.on_press = self.ajsf

    def ajsf(self):
        print(
            f"{str(self.piece_color)} {str(self.species)} index: {self.parent.children.index(self)}"
        )
        myparent = self.parent
        myindex = myparent.children.index(self)

        myparent.remove_widget(self)

        myparent.add_widget(Widget(), myindex)


class PieceColor(Enum):
    """This allows the color to also be used like a bool, but preferred to be a enum"""

    BLACK = 0
    WHITE = 1


class PieceSpecies(Enum):
    """It has self casting, i.e if 'PieceSpecies' is called with a parramater,
      of a string it can be casted as that species.

    Note: i wanted the call it 'PieceClass' but class is protected (i wonder why /s)
      and it interferred with the 'Piece' class
    """

    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


if __name__ == "__main__":
    print(Piece("Images/b_pawn.png"))
