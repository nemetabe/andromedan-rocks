from .system import System
from ..components import PlayerControlled, Direction
from ..events import MoveIntentEvent, ShootCommandEvent


class InputSystem(System):
    def __init__(self, world, input):
        super().__init__(world)
        self.input = input

    def update(self, dt):
        self.input.poll()

        for entity in self.world.query(PlayerControlled):
            self._handle_entity_input(entity)

        self.input.clear()

    def _handle_entity_input(self, entity):
        keys = self.input.pressed_keys

        dx = dy = 0

        if 'a' in keys:
            dx -= 1
        if 'd' in keys:
            dx += 1
        if 'w' in keys:
            dy -= 1
        if 's' in keys:
            dy += 1

        if dx != 0 or dy != 0:
            self.world.event_bus.emit(
                MoveIntentEvent(entity, dx, dy)
            )
        else:
            self.world.event_bus.emit(
            StopIntentEvent(entity)
            )

        if ' ' in keys:
            self.world.event_bus.emit(
                ShootCommandEvent(entity)
            )
