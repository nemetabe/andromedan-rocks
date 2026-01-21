from ..core.abc_esc.entity import Entity
from ..components import Position, Velocity, Health
from ..components import Renderable, Collider, PlayerControlled


class SpaceShip(Entity): 
    def __init__(self, x, y):
        super().__init__()

        self.add(Position(x, y))
        self.add(Velocity(0, 0))
        self.add(Collider(width=2, height=1))
        self.add(Health(1))
        self.add(PlayerControlled())
        self.add(Renderable("+"))
