from piece_enums import PieceColor, PieceSpecies


class Behavior:
    last_caller = None

    @staticmethod
    def tile_clicked(caller):

        match caller.species:
            case PieceSpecies.BLANK:
                return
            case PieceSpecies.PAWN:
                Pawn(caller)
        Behavior.last_caller = caller

    @staticmethod
    def swap_tiles(tile1, tile2):
        tile1_index = tile1.parent.children.index(tile1)
        tile2_index = tile2.parent.children.index(tile2)

        parent = tile1.parent

        parent.remove_widget(tile1)
        parent.remove_widget(tile2)

        if tile1_index < tile2_index:
            parent.add_widget(tile2, tile1_index)
            parent.add_widget(tile1, tile2_index)
        else:
            parent.add_widget(tile1, tile2_index)
            parent.add_widget(tile2, tile1_index)


class Pawn:
    def __init__(self, caller):
        caller_index = caller.parent.children.index(caller)
        print(caller_index)


class Rook:
    pass


class Knight:
    pass


class Bishop:
    pass


class Queen:
    pass


class King:
    pass
