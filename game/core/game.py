class Game:
	def __init__(self, time, input_system, movement_system, world, event_bus):
		self.time = time
		self.input = input_system
		self.movement = movement_system
		self.event_bus = event_bus
		self.world = world
		self.running = True

	def run(self):
		self.time.reset()

		while self.running:
			dt = self.time.tick()

			self.update(dt)
			self.render()

	def update(self, dt):
		self.input.update(dt)
		self.world.update(dt)
		self.movement.update(dt)
		self.event_bus.flush()

	def render(self):
		pass