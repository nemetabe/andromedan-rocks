class Game:
	def __init__(
		self,
		time,
		input_system,
		movement_system,
		world,
		event_bus,
		game_state,
	):
		self.time = time
		self.input = input_system
		self.movement = movement_system
		self.event_bus = event_bus
		self.world = world
		self.state = game_state
		self.running = True

	def run(self):
		self.time.reset()

		while self.running:
			dt = self.time.tick()

			self.update(dt)
			self.render(world=self.world, game_state=self.state)

	def update(self, dt):
		self.input.update(dt)
		self.world.update(dt)
		self.movement.update(dt)
		self.event_bus.flush()

	def render(self, world, game_state):
		print("Score :", game_state.score)
		print("Lives :", game_state.lives)
		print("Entities :", len(world.entities))