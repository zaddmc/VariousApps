from piece_enums import PieceColor, PieceSpecies
from piece_movement import MovementHandler


class Behavior:
    last_call = None

    @staticmethod
    def tile_clicked(caller):
        if Behavior.last_call:
            Behavior.last_call.follow_up(caller)

        match caller.species:
            case PieceSpecies.BLANK:
                print("I AM BLANK", caller.get_index())

            case PieceSpecies.PAWN:
                Behavior.last_call = Pawn(caller)
            case PieceSpecies.ROOK:
                Behavior.last_call = Rook(caller)
            case PieceSpecies.KNIGHT:
                Behavior.last_call = Knight(caller)
            case PieceSpecies.BISHOP:
                Behavior.last_call = Bishop(caller)
            case PieceSpecies.QUEEN:
                Behavior.last_call = Queen(caller)
            case PieceSpecies.KING:
                Behavior.last_call = King(caller)


class PieceAction:
    def __init__(self, caller):
        self.innitiater = caller
        caller_index = caller.get_index()
        print(caller_index)
        self.possible_tiles = set()

    def follow_up(self, caller):
        print(
            f"innitiater: {self.innitiater.get_index()}  "
            + f"Other: {caller.get_index()}"
        )
        MovementHandler.move_tile(self.innitiater, caller)

    def find_possible_tiles(self):
        NotImplementedError("This function should be implemented by an inherinter")

    def get_possible_tiles(self):
        return self.possible_tiles


class Pawn(PieceAction):
    def find_possible_tiles(self):
        pass

    def forward(self):
        pass


class Rook(PieceAction):
    pass


class Knight(PieceAction):
    pass


class Bishop(PieceAction):
    pass


class Queen(PieceAction):
    pass


class King(PieceAction):
    pass
