from .component import Component


class PositionComponent(Component):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y