from core import Game, EventBus, World
from entities import SpaceShip
from systems import InputSystem, MovementSystem, TimeSystem


def main():
	event_bus = EventBus()

	space_ship = SpaceShip(event_bus)
	world = World([space_ship])
	
	input_sytem = InputSystem(event_bus)
	movement_system = MovementSystem(world)
	time_system = TimeSystem()

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
