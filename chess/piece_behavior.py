class Behavior:
    last_caller = None

    @staticmethod
    def tile_clicked(caller):
        print(caller.parent.children.index(caller))


class PawnBehavior(Behavior):
    pass
