from ..events import CollisionEvent, AsteroidHitEvent
from ..components import Hostile, PlayerControlled


class AsteroidHitSystem:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        event_bus.subscribe(CollisionEvent, self.on_collision)

    def on_collision(self, event):
        a, b = event.a, event.b

        if self._is_hostile_vs_player(a, b):
            self.event_bus.emit(AsteroidHitEvent(asteroid=a, other=b))
        elif self._is_hostile_vs_player(b, a):
            self.event_bus.emit(AsteroidHitEvent(asteroid=b, other=a))

    def _is_hostile_vs_player(self, a, b):
        return a.has(Hostile) and b.has(PlayerControlled)
