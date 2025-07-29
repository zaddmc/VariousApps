from piece_enums import PieceColor, PieceSpecies


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

    @staticmethod
    def swap_tiles(tile1, tile2):
        tile1_index = tile1.get_index()
        tile2_index = tile2.get_index()

        parent = tile1.parent

        parent.remove_widget(tile1)
        parent.remove_widget(tile2)

        if tile1_index < tile2_index:
            parent.add_widget(tile2, tile1_index)
            parent.add_widget(tile1, tile2_index)
        else:
            parent.add_widget(tile1, tile2_index)
            parent.add_widget(tile2, tile1_index)

    @staticmethod
    def move_tile(origin, dest):
        """'origin' is a piece that should be moved, leaving a blank in its place
        'dest' can be another piece/blank or an index for the first piece to move to
        Note: This function will not validate the given move,
        it will only ensure it is whitin bounderies
        """

        dest_index = dest if isinstance(dest, int) else dest.parent.children.index(dest)
        if 0 > dest_index >= 63:
            IndexError(f"'dest_index' is out of bounds ({dest_index})")

        orig_index = origin.get_index()


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
