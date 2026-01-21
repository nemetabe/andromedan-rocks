from .view_port import ViewPort


class Display:
    def __init__(self, world, width: int, height: int):
        self.width = width
        self.height = height
        self.world = world
        self.view_port = self._build_view_port()

    def _build_view_port(self):
        return ViewPort(self.world, 32, 32)

    def display(self):
        return self.view_port.draw_display()
