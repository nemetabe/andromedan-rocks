from .component import Component


class VelocityComponent(Component):
    def __init__(self, dx: float = 0, dy: int = 0):
        self.dx = dx
        self.dy = dy