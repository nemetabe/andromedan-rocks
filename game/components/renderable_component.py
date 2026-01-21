from ..core import Component


class Renderable(Component):
    def __init__(self, symbol: str):
        self.symbol = symbol