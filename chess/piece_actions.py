from piece_enums import PieceColor, PieceSpecies
from piece_movement import MovementHandler


class Behavior:
    last_call = None

    @staticmethod
    def tile_clicked(caller):
        if Behavior.last_call:
            Behavior.last_call.follow_up(caller)
            Behavior.last_call = None
            return

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
    """Base actions for the other actions"""

    def __init__(self, caller):
        self.innitiater = caller
        caller_index = caller.get_index()
        print(f"{caller.piece_color} {caller.species} index: {caller_index}")
        self.possible_tiles = set()
        self.find_possible_tiles()
        print(self.possible_tiles)

    def follow_up(self, caller):
        print(
            f"innitiater: {self.innitiater.get_index()}",
            f"Other: {caller.get_index()}",
        )
        if caller.get_index() in self.possible_tiles:
            MovementHandler.move_tile(self.innitiater, caller)
            self.innitiater.moves += 1

    def find_possible_tiles(self):
        raise NotImplementedError(
            "This function should be implemented by an inherinter"
        )

    def get_relative_index(self, check):
        modifier = 1 if self.innitiater.piece_color == PieceColor.WHITE else -1
        return self.innitiater.get_index() + (check * modifier)

    def get_relative(self, check):
        return self.innitiater.get_sibling(self.get_relative_index(check))

    def add_rel_tile(self, index):
        self.possible_tiles.add(self.get_relative_index(index))

    def assume_tile(self, index: int):
        """Assume tile to check is blank"""
        if self.get_relative(index).species == PieceSpecies.BLANK:
            self.add_rel_tile(index)

    def assume_enemy(self, index: int):
        if self.get_relative(index).species != PieceSpecies.BLANK:
            self.add_rel_tile(index)


class Pawn(PieceAction):
    def find_possible_tiles(self):
        self.forward()
        self.double_forward()
        self.attack()
        self.en_passant()

    def forward(self):
        self.assume_tile(8)

    def double_forward(self):
        if self.innitiater.moves:
            return
        if self.get_relative(8).species == PieceSpecies.BLANK:
            self.assume_tile(16)

    def attack(self):
        self.assume_enemy(7)
        self.assume_enemy(9)

    def en_passant(self):
        def validate(pawn_index):
            pawn = self.get_relative(pawn_index)
            if pawn.species == PieceSpecies.PAWN and pawn.moves == 1:
                self.add_rel_tile(pawn_index + 8)

        validate(1)
        validate(-1)


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
