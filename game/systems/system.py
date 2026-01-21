from abc import ABC, abstractmethod


class System(ABC):
    """Base system (pure logic)"""
    def __init__(self, world):
        self.world = world
    
    @abstractmethod
    def update(self, dt: float):
        """Update with delta time"""
        pass