from my_enums import Actions, PieceColor, PieceSpecies
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
                caller.highligt_me()

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
        self.possible_tiles = {}
        self.find_possible_tiles()

        print(self.possible_tiles)

    def follow_up(self, caller):
        caller_index = caller.get_index()

        if caller_index in self.possible_tiles.keys():
            values = self.possible_tiles[caller_index]
            action = values[0]
            special_tile = values[1] if len(values) > 1 else None

            self.innitiater.remove_highlights()

            match action:
                case Actions.MOVE | Actions.ATTACK:
                    MovementHandler.move_tile(self.innitiater, caller)
                    self.innitiater.moves += 1
                case Actions.ENPASSANT:
                    self.handle_en_passant(caller, special_tile)
                    self.innitiater.moves += 1
                case Actions.CASTLING:
                    pass
                case x:
                    raise NotImplementedError(f"Should not exist {x}")

    def find_possible_tiles(self):
        print("This piece does not have logic")

    def get_relative_index(self, check):
        modifier = 1 if self.innitiater.piece_color == PieceColor.WHITE else -1
        return self.innitiater.get_index() + (check * modifier)

    def get_relative(self, check):
        return self.innitiater.get_sibling(self.get_relative_index(check))

    def add_rel_tile(self, index: int, action: Actions, special_tile: int = None):
        rel_index = self.get_relative_index(index)
        assignmet = [action, special_tile] if special_tile else [action]
        self.possible_tiles[rel_index] = assignmet

    def assume_blank(self, index: int):
        """Assume tile to check is blank"""
        rel_index = self.get_relative_index(index)
        if not (0 <= rel_index <= 63):
            return False

        if self.innitiater.get_sibling(rel_index).species == PieceSpecies.BLANK:
            self.add_rel_tile(index, Actions.MOVE)
            return True
        return False

    def assume_enemy(self, index: int):
        rel_index = self.get_relative_index(index)
        if not (0 <= rel_index <= 63):
            return False

        other = self.get_relative(index)
        if other.species == PieceSpecies.BLANK:
            return False
        if self.innitiater.piece_color == other.piece_color:
            return False
        self.add_rel_tile(index, Actions.ATTACK)
        return True

    def assume_any(self, index: int):
        if self.assume_blank(index):
            return True
        if self.assume_enemy(index):
            return True
        return False

    def assume_diagonal(self):
        pass


class Pawn(PieceAction):
    def find_possible_tiles(self):
        self.forward()
        self.double_forward()
        self.attack()
        self.en_passant()

    def forward(self):
        self.assume_blank(8)

    def double_forward(self):
        if self.innitiater.moves:
            return
        if self.get_relative(8).species == PieceSpecies.BLANK:
            self.assume_blank(16)

    def attack(self):
        self.assume_enemy(7)
        self.assume_enemy(9)

    def en_passant(self):
        def validate(pawn_index):
            pawn = self.get_relative(pawn_index)
            if pawn.species == PieceSpecies.PAWN and pawn.moves == 1:
                self.add_rel_tile(pawn_index + 8, Actions.ENPASSANT, pawn.get_index())

        validate(1)
        validate(-1)

    def handle_en_passant(self, caller, special_tile):
        caller_index = caller.get_index()
        MovementHandler.swap_tiles(caller, caller.get_sibling(special_tile))
        MovementHandler.move_tile(self.innitiater, caller_index)


class Rook(PieceAction):
    def find_possible_tiles(self):
        pass


class Knight(PieceAction):
    pass


class Bishop(PieceAction):
    pass


class Queen(PieceAction):
    pass


class King(PieceAction):
    pass
