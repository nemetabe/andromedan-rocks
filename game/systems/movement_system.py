from core import System
from events import EntityMovedEvent, MovementBockedEvent
from components import Position, Motion, Direction


class MovementSystem(System):
    """
    applies velocity to position (uses dt for frame-independent movement)
    """
    def __init__(self, world):
        super().__init__(world)

    def on_move_intent_event(self, event):
        entity = event.entity

        if not entity.has(Direction):
            return

        direction = entity.get(Direction)

        direction.x = event.dx
        direction.y = event.dy

    def update(self, dt: float):
        for entity in self.world.query(Position, Motion, Direction):
            old_pos = entity.get(Position)
            speed = entity.get(Motion)
            displacement = entity.get(Direction)

            # calculate the length of the vector of displacement
            distance = speed.speed

            # calculate end point of the vector of displacement
            # relativ to the position
            dx = int(old_pos.x + (distance * displacement.x)*dt)
            dy = int(old_pos.y + (distance * displacement.y)*dt)

            if self.world.map_manager.is_walkable(
                    old_pos.x + dx,
                    old_pos.x + dy):
                new_pos = entity.get(Position)
                new_pos.x += dx
                new_pos.y += dy
                self.world.event_bus.emit(
                    EntityMovedEvent(entity, old_pos, new_pos))
            else:
                self.world.event_bus.emit(  
                    MovementBockedEvent(entity, "Not walkable")
                )
