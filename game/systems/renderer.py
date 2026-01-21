from .system import System
from ..core import Display
from abc import abstractmethod, ABC


class Renderer(System, ABC):
    def __init__(self, world, display: Display):
        super().__init__(world)
        self.display = display

    @abstractmethod
    def render(self, world):
        pass
