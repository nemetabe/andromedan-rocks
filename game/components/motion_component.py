from ..core import Component


class Velocity(Component):
    def __init__(self, v: int = 1):
        self.v = v
