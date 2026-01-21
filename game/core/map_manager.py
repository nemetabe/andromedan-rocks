from ..components import Renderable, Position
from .map import Map


class MapManager:
    """
    manages the game map
    handles map generation, tiles, spatial queries
    """
    def __init__(self, width, height):
        self.area_width = width
        self.area_height = height
        self.border = 2
        self.total_width = self.area_width + 2 * self.border
        self.total_height = self.area_height + 2 * self.border
        self._init_map()

    def _init_map(self):
        self._get_new_map()

    def _get_new_map(self) -> Map:
        self.map = Map(self.total_width, self.total_height)
        self.map.coordinates = self._build_map()

    # fills map coordinates
    def _build_map(self):
        rows = []
        for y in range(self.total_height):
            row = []
            for x in range(self.total_width):
                if (
                    x < self.border or
                    x >= self.border + self.area_width or
                    y < self.border or
                    y >= self.border + self.area_height
                ):
                    row.append("#")
                else:
                    row.append(" ")
            rows.append(row)
        return rows
            
    def is_walkable(self, x: int, y: int) -> bool:
        """check if position is walkable"""
        if 0 <= x < self.total_width and 0 <= y < self.total_height:
            return self.map.coordinates[y][x] != '#'
        return False

    def get_tile(self, x: int, y: int) -> str:
        """get tile at position"""
        if 0 <= x < self.total_width and 0 <= y < self.total_height:
            return self.map.coordinates[y][x]
        return "."
# todo

    def set_tile(self, x: int, y: int, tile: str):
        """set tile at position"""
        if 0 <= x < self.total_width and 0 <= y < self.total_height:
            self.map.coordinates[y][x] = tile

    def add_entity_positions(self, entities):
        """adds entities renderable at location on manager tiles for render"""
        for entity in entities:
            pos = entity.get(Position)
            tile = entity.get(Renderable).sprite
            self.set_tile(pos.x, pos.y, tile)

            print(f"{tile} at ({pos.x}, {pos.y})")

    def on_entity_spawned_event(self, event):
        entity = event.entity

        if entity.has(Renderable) and entity.has(Position):
            sprite = entity.get(Renderable).sprite
            pos = entity.get(Position)
            self.set_tile(pos.x, pos.y, sprite)

    def on_entity_destroyed_event(self, event):
        entity = event.entity

        if entity.has(Renderable) and entity.has(Position):
            sprite = entity.get(Renderable).sprite
            pos = entity.get(Position)
            if self.get_tile(pos.x, pos.y) == sprite:
                self.set_tile(pos.x, pos.y, " ")

    def on_entity_moved_event(self, event):
        entity = event.entity
        old_p = event.old_pos
        new_p = event.new_pos

        if entity.has(Renderable):
            sprite = entity.get(Renderable).sprite
            self.set_tile(old_p.y, old_p.x, " ")
            self.set_tile(new_p.y, new_p.x, sprite)
