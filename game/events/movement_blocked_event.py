from core import Event


class MovementBockedEvent(Event):
    def __init__(self, entity, reason):
        super().__init__()
        self.entity = entity
        self.reason = reason
