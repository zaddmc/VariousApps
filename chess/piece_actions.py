from my_enums import Actions, PieceColor, PieceSpecies
from piece_movement import MovementHandler as MH


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
        self.grid_size = caller.grid_size
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
                    MH.move_tile(self.innitiater, caller)

                    # Bit of a hack, but works
                    if self.innitiater.species == PieceSpecies.PAWN:
                        self.handle_promotion()

                case Actions.ENPASSANT:
                    self.handle_en_passant(caller, special_tile)

                case Actions.CASTLING:
                    pass

                case x:
                    raise NotImplementedError(f"Should not exist {x}")

            self.innitiater.moves += 1

    def find_possible_tiles(self):
        print("This piece does not have logic")

    def get_relative_index(self, check: tuple):
        modifier = 1 if self.innitiater.piece_color == PieceColor.WHITE else -1
        x, y = divmod(self.innitiater.get_index(), self.grid_size)

        # Legacy code
        if isinstance(check, int):
            raise TypeError("int is no longer an accepted type in this function")
            rel_index = self.innitiater.get_index() + (check * modifier)
            if not (0 <= rel_index < self.grid_size * self.grid_size - 1):
                return None
            return rel_index

        x += check[0] * modifier
        y += check[1] * modifier

        if not (0 <= x < self.grid_size):
            return None
        if not (0 <= y < self.grid_size):
            return None

        return x * self.grid_size + y

    def get_relative(self, check):
        rel_index = self.get_relative_index(check)
        if rel_index == None:
            return None
        if not (0 <= rel_index <= 63):
            return None
        return self.innitiater.get_sibling(rel_index)

    def add_rel_tile(self, index: int, action: Actions, special_tile: int = None):
        rel_index = self.get_relative_index(index)
        self.add_tile(rel_index, action, special_tile)

    def add_tile(self, rel_index: int, action: Actions, special_tile: int = None):
        assignmet = [action, special_tile] if special_tile else [action]
        self.possible_tiles[rel_index] = assignmet

        self.innitiater.get_sibling(rel_index).highligt_me(action)

    def assume_blank(self, index: int):
        """Assume tile to check is blank"""
        rel_index = self.get_relative_index(index)
        if rel_index == None:
            return None

        if self.innitiater.get_sibling(rel_index).species == PieceSpecies.BLANK:
            self.add_tile(rel_index, Actions.MOVE)
            return True
        return False

    def assume_enemy(self, index: int):
        rel_index = self.get_relative_index(index)
        if rel_index == None:
            return None
        if not (0 <= rel_index <= 63):
            return False

        other = self.innitiater.get_sibling(rel_index)
        if other.species == PieceSpecies.BLANK:
            return False
        if self.innitiater.piece_color == other.piece_color:
            return False
        self.add_tile(rel_index, Actions.ATTACK)
        return True

    def assume_any(self, index: int):
        if self.assume_blank(index):
            return Actions.MOVE
        if self.assume_enemy(index):
            return Actions.ATTACK
        return False

    def assume_any_diagonal(self, direction: tuple):
        def tmul(base: tuple, multiplier: int):
            return tuple(a * multiplier for a in base)

        i = 1
        while self.assume_any(tmul(direction, i)) == Actions.MOVE:
            i += 1


class Pawn(PieceAction):
    def find_possible_tiles(self):
        self.forward()
        self.double_forward()
        self.attack()
        self.en_passant()

    def forward(self):
        self.assume_blank((1, 0))

    def double_forward(self):
        if self.innitiater.moves:
            return
        if self.get_relative((1, 0)).species == PieceSpecies.BLANK:
            self.assume_blank((2, 0))

    def attack(self):
        self.assume_enemy((1, 1))
        self.assume_enemy((1, -1))

    def en_passant(self):
        def validate(pawn_index):
            pawn = self.get_relative((0, pawn_index))
            if not pawn:
                return

            if pawn.species == PieceSpecies.PAWN and pawn.moves == 1:
                self.add_rel_tile((1, pawn_index), Actions.ENPASSANT, pawn.get_index())

        validate(1)
        validate(-1)

    def handle_en_passant(self, caller, special_tile):
        caller_index = caller.get_index()
        MH.swap_tiles(caller, caller.get_sibling(special_tile))
        MH.move_tile(self.innitiater, caller_index)

    def handle_promotion(self):
        if self.innitiater.get_index() // self.grid_size in [0, 7]:
            MH.promote(self.innitiater)


class Rook(PieceAction):
    def find_possible_tiles(self):
        self.moves()

    def moves(self):
        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.assume_any_diagonal(dir)


class Knight(PieceAction):
    def find_possible_tiles(self):
        self.moves()

    def moves(self):
        # pre generated list cuz im lazy
        m = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for spot in m:
            self.assume_any(spot)


class Bishop(PieceAction):
    def find_possible_tiles(self):
        self.moves()

    def moves(self):
        for dir in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
            self.assume_any_diagonal(dir)


class Queen(PieceAction):
    pass


class King(PieceAction):
    pass
