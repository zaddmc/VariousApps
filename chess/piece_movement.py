from piece_generator import BasePiece, Blank, Piece


class MovementHandler:
    @staticmethod
    def swap_tiles(tile1: BasePiece, tile2: BasePiece):
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
    def move_tile(origin: Piece, dest: int | BasePiece):
        """'origin' is a piece that should be moved, leaving a blank in its place
        'dest' can be another piece/blank or an index for the first piece to move to
        Note: This function will not validate the given move,
        it will only ensure it is whitin bounderies
        """

        dest_index = dest if isinstance(dest, int) else dest.get_index()
        if 0 > dest_index >= 63:
            raise IndexError(f"'dest_index' is out of bounds ({dest_index})")

        parent = origin.parent

        orig_index = origin.get_index()
        parent.remove_widget(origin)
        parent.add_widget(Blank(), orig_index)

        parent.remove_widget(parent.children[dest_index])
        parent.add_widget(origin, dest_index)

    @staticmethod
    def promote(origin: Piece):
        idx = origin.get_index()
        parent = origin.parent

        promoter = Promoter()
        promoter.dropdown.open(origin)

        def on_choice(instance, choice, origin=origin):
            color = origin.piece_color

            parent.remove_widget(origin)
            del origin

            choice = f"Images/{str(color)[11].lower()}_{choice.lower()}.png"
            parent.add_widget(Piece(choice), idx)

        promoter.dropdown.bind(on_select=on_choice)


class Promoter:
    from kivy.uix.button import Button
    from kivy.uix.dropdown import DropDown

    def __init__(self):
        self.dropdown = self.DropDown()
        for item in ["Queen", "Bishop", "Knight", "Rook"]:
            btn = self.Button(text=item, size_hint_y=None)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
