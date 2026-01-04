from core import Event


class MoveIntentEvent(Event):
    def __init__(self, entity, dx, dy):
        super().__init__()
        self.enitity = entity
        self.dx = dx
        self.dy = dy
