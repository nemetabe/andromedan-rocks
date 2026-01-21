from core import Component


class Direction(Component):
    def __init__(self, dx: int = 0, dy: int = 0):
        self.dx: dx
        self.dy: dy