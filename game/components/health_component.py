from .component import Component


class HealthComponent(Component):
    def __init__(self, hp: int, max_hp: int):
        self.hp = hp
        self.max_hp = max_hp