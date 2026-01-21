from ..entities import SpaceShip, Asteroid
# from ..components import Position, Direction, Health, Motion
from ..components import PlayerControlled, Hostile
# from ..components import AiControlled
# Collider


class EntityFactory:
    """
    factory pattern for creating entities
    centralizes entity blueprints
    """
    def __init__(self, world):
        self.world = world

    @staticmethod
    def create_player_space_ship(x: int, y: int) -> SpaceShip:
        """create player entity"""
        player = SpaceShip(x=x, y=y)
        player.add(PlayerControlled)
        return player

    @staticmethod
    def create_enemy_asteroid(x: int, y: int) -> Asteroid:
        """create enemy entity"""
        enemy = Asteroid(x=x, y=y)
        # entity.add(AiControlled())
        enemy.add(Hostile())
        return enemy
