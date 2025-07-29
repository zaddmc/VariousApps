from enum import Enum


class PieceColor(Enum):
    """This allows the color to also be used like a bool, but preferred to be a enum"""

    BLACK = 0
    WHITE = 1
    BLANK = -1


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
    BLANK = "blank"
