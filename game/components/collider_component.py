from ..core import Component


class Collider(Component):
    def __init__(self, width, height):
        self.width = width
        self.height = height