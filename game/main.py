from .core import Game, World, GameState
from .core.clock import Clock
from .systems.terminal_renderer import TerminalRenderer

from .events import MoveIntentEvent
from .events import DebugEventLogger
from .events import EntityMovedEvent
from .events import Event
from .events import CollisionEvent
from .events import EntityDestroyedEvent
from .events import AsteroidSpawnedEvent

from .core.entity_factory import EntityFactory

from .systems.movement_system import MovementSystem
from .systems.asteroid_spawn_system import AsteroidSpawnSystem
from .systems.collision_system import CollisionSystem
from .systems.collision_rules_system import CollisionRulesSystem
from .systems.input_system import InputSystem
from .systems.terminal_input import TerminalInput


def main():
    # -------------------------
    # infrastructure
    # -------------------------
    clock = Clock()
    world = World(width=60, height=30)
    player = EntityFactory.create_player_space_ship(x=30, y=4)
    world.add_player(player)

    # -------------------------
    # input (platform-specific)
    # -------------------------
    terminal_input = TerminalInput(world)
    terminal_input.start()

    input_system = InputSystem(world, terminal_input)

    # -------------------------
    # game systems
    # -------------------------
    movement_system = MovementSystem(world)
    asteroid_spawn_system = AsteroidSpawnSystem(world)
    collision_system = CollisionSystem(world)
    collision_rules_system = CollisionRulesSystem(event_bus=world.event_bus)

    renderer = TerminalRenderer(world)
    game_state = GameState(world.event_bus)
    debug_event_logger = DebugEventLogger(world.event_bus)
    # -------------------------
    # event wiring
    # -------------------------
    world.event_bus.subscribe(
        Event,
        debug_event_logger.log
    )
    world.event_bus.subscribe(
        MoveIntentEvent,
        movement_system.on_move_intent_event
    )
    world.event_bus.subscribe(
        EntityMovedEvent,
        world.map_manager.on_entity_moved_event
    )
    world.event_bus.subscribe(
        EntityDestroyedEvent,
        world.map_manager.on_entity_destroyed_event
    )
    world.event_bus.subscribe(
        AsteroidSpawnedEvent,
        world.map_manager.on_entity_spawned_event
    )

    # -------------------------
    # game
    # -------------------------
    game = Game(
        time=clock,
        input_system=input_system,
        movement_system=movement_system,
        collision_system=collision_system,
        renderer=renderer,
        asteroid_spawn_system=asteroid_spawn_system,
        world=world,
        game_state=game_state,
    )

    # -------------------------
    # run
    # -------------------------
    try:
        game.run()
    finally:
        terminal_input.stop()
