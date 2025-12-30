from ..core import Component


class Velocity(Component):
    def __init__(self, dx: float = 0, dy: int = 0):
        self.dx = dx
        self.dy = dy