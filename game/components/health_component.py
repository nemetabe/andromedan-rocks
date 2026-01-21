from ..core import Component


class Health(Component):
    def __init__(self, hp: int):
        self.hp = hp