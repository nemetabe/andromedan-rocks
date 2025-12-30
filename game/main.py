from core import Game, GameState, EventBus, World
from entities import SpaceShip
from events import AsteroidHitEvent, AsteroidAvoidedEvent
from systems import InputSystem, MovementSystem, Clock


def main():
	event_bus = EventBus()

	game_state = GameState()
	event_bus.subscribe(AsteroidHitEvent, game_state.on_asteroid_hit)
	event_bus.subscribe(AsteroidAvoidedEvent, game_state.on_asteroid_avoided)
	
	space_ship = SpaceShip(event_bus)
	world = World([space_ship])
	
	input_sytem = InputSystem(event_bus)
	movement_system = MovementSystem(world)
	time_system = Clock()

	game = Game(
		time=time_system,
		input=input_sytem,
		movement=movement_system,
		world=world,
		event_bus=event_bus
	)

	game.run()


if __name__ == "__main__":
	main()
