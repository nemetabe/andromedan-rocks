import os
from ..core import Display
from .renderer import Renderer


class TerminalRenderer(Renderer):
    def __init__(self, world):
        display = Display(world, 40, 20)
        super().__init__(world, display=display)

        self.screen = []

    def update(self):
        self.screen = self.display.display()
        self.render(self.world)

    def render(self, world):
        os.system('clear')

        print("\n---")
        for y in range(len(self.screen)):
            row = []
            for x in range(len(self.screen[y])):
                row.append(self.screen[y][x])

            print("".join(row))

        print("\n---")
        print("move!")
