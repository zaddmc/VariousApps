class Behavior:
    last_caller = None

    @staticmethod
    def tile_clicked(caller):
        print(caller.parent.children.index(caller))
        if caller and Behavior.last_caller:
            Behavior.swap_tiles(caller, Behavior.last_caller)
            Behavior.last_caller = None
            return

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
    pass


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
