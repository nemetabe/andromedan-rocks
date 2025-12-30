from core import Entity
from components import Position, Velocity, Collider, Hostile


class Asteroid(Entity):
    def __init__(self, x, y, speed):
        super().__init__()

        self.add(Position(x, y))
        self.add(Velocity(0, -speed))
        self.add(Collider(width=2, height=2))
        self.add(Hostile())