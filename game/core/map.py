class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coordinates = []

    @property
    def get_coordinates(self):
        return self.coordinates
