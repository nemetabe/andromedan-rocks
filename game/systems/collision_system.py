from ..events import CollisionEvent
from .system import System
from ..entities import Entity
from ..components import Position, Collider


class CollisionSystem(System):
    def __init__(self, world):
        self.world = world
        self.event_bus = world.event_bus

    def update(self):
        entities = self.world.entity_manager.entities

        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                a, b = entities[i], entities[j]

                if self._collides(a, b):
                    self.event_bus.emit(CollisionEvent(a, b))

    def _collides(self, a: Entity, b: Entity):
        box_a = self._get_bounding_box(a)
        box_b = self._get_bounding_box(b)
        
        if not box_a or not box_b:
            return False
        
        ax, ay, aw, ah = box_a
        bx, by, bw, bh = box_b

        return (
            ax < bx + bw and
            ax + aw > bx and
            ay < by + bh and
            ay + ah > by
        )

    def _get_bounding_box(self, entity):
        pos = entity.get(Position)
        col = entity.get(Collider)

        if not pos or not col:
            return None

        return pos.x, pos.y, col.width, col.height
