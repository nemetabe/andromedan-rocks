from ..components import Position


class ViewPort():
    """ x_a + player_x + x_z = width"""
    """ x_y + player_y + y_z = width"""

    def __init__(self, world, w, h):
        self.width = w
        self.height = h
        self.world = world

    def draw_display(self):
        self.update()
        display = []

        start_y = int(self.y_a)
        end_y = int(self.y_a + self.height)
        for y in range(start_y, end_y):
            row = []

            start_x = int(self.x_a)
            end_x = int(self.x_a + self.width + 1)
            if y >= self.y_a or y <= self.y_z:
                for x in range(start_x, end_x):

                    if x >= self.x_a and x <= self.x_z:
                        tile = self.world.get_tile(x, y)
                        row.append(tile)

            display.append(row)
        return display

    def update(self):
        self.player = self.world.get_player()
        self.player_x = self.player.get(Position).x
        self.player_y = self.player.get(Position).y
        self.x_a = self.player_x - (self.width / 2)
        self.x_z = self.player_x + (self.width / 2)
        self.y_a = self.player_y - (self.height / 2) - 1
        self.y_z = self.player_y + 4
