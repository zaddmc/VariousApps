from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget

from piece_behavior import Behavior
from piece_enums import PieceColor, PieceSpecies


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


class Blank(ButtonBehavior, Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.species: PieceSpecies = PieceSpecies.BLANK
        self.piece_color: PieceColor = PieceColor.BLANK

    def on_press(self):
        Behavior.tile_clicked(self)


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

    def on_press(self):
        Behavior.tile_clicked(self)


if __name__ == "__main__":
    print(Piece("Images/b_pawn.png"))
