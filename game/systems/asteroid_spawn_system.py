from ..events import AsteroidSpawnedEvent
from ..entities import Asteroid
from .system import System
from ..core import EntityFactory
from random import randint


class AsteroidSpawnSystem(System):
    def __init__(self, world):
        self.world = world
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer > 20:
            self.timer = 0
            asteroid = self.create_asteroid()
            self.world.add_entity(asteroid)
            self.world.event_bus.emit(AsteroidSpawnedEvent(asteroid))

    def create_asteroid(self) -> Asteroid:
        w = int(self.world.map_manager.area_width / 2)
        b = self.world.map_manager.border
        m_w = w * 3
        h = int(self.world.map_manager.area_height / 2)
        x_a = b + w
        x_b = m_w + b
        return EntityFactory.create_enemy_asteroid(
            x=randint(x_a, x_b), y=randint(b, h))
