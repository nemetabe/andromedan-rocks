from .entity_manager import EntityManager
from .event_bus import EventBus
from .map_manager import MapManager
from ..entities import Entity, SpaceShip
from ..components import PlayerControlled


class World:
    """
    central hub containing all game state
    """
    def __init__(self, width: int, height: int):
        self.entity_manager = EntityManager()
        self.map_manager = MapManager(width, height)
        self.event_bus = EventBus()
        
    def add_entity(self, entity) -> Entity:
        return self.entity_manager.add_entity(entity)

    def destroy_entity(self, entity: Entity):
        self.entity_manager.destroy_entity(entity)

    def query(self, *component_types):
        return self.entity_manager.query(*component_types)

    def get_tile(self, x, y):
        return self.map_manager.get_tile(x, y)

    def add_player(self, player):
        self.player = self.add_entity(player)

    def get_player(self) -> SpaceShip:
        return self.player

    def update(self, dt: float):
        """update world state (cleanup dead entities)"""
        self.entity_manager.cleanup()

    def get_all_entities(self):
        """easy access to entities"""
        return self.entity_manager.get_all_entities()
