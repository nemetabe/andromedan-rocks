from .component import Component


class RenderableComponent(Component):
    def __init__(self, symbol: str):
        self.symbol = symbol