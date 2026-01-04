from core import Event


class EntityMovedEvent(Event):
    def __init__(self, entity, old_pos, new_pos):
        super().__init__()
        self.entity = entity
        self.old_pos = old_pos
        self.new_pos = new_pos
