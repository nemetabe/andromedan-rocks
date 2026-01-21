from ..events import CollisionEvent, AsteroidHitEvent, CollectiblePickedEvent
from ..events import SpaceShipHitEvent
from ..components import Hostile, Collectible, PlayerControlled

COLLISION_RULES = [
    ((Hostile, PlayerControlled), AsteroidHitEvent),
    ((PlayerControlled, Hostile), SpaceShipHitEvent),
    ((Collectible, PlayerControlled), CollectiblePickedEvent)

]


class CollisionRulesSystem:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        event_bus.subscribe(CollisionEvent, self.on_collision)

    def on_collision(self, event):
        a, b = event.a, event.b

        for (a_comp, b_comp), event_cls in COLLISION_RULES:
            if a.has(a_comp) and b.has(b_comp):
                self.event_bus.emit(event_cls(a=a, b=b))
            elif b.has(a_comp) and a.has(b_comp):
                self.event_bus.emit(event_cls(a=b, b=a))