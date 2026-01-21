from ..entities import Entity


class EntityManager:
    """
    manages entity lifecycle: create, destroy, query
    """
    def __init__(self):
        self.entities: list[Entity] = []
        self.entities_to_remove: list[Entity] = []

    def add_entity(self, entity):
        """factory method for adding entities"""
        self.entities.append(entity)
        return entity

    def create_entity(self, *components) -> Entity:
        """factory method for creating entities"""
        entity = Entity()
        for comp in components:
            entity.add(comp)

        self.entities.append(entity)
        return entity

    def destroy_entity(self, entity: Entity):
        """mark entity for removal (processed at the end of frame)"""
        self.entities_to_remove.append(entity)

    def cleanup(self):
        """remove entities marked for removel"""
        for entity in self.entities_to_remove:
            if entity in self.entities:
                self.entities.remove(entity)
        self.entities_to_remove.clear()

    def query(self, *components):
        """gets entities with given components present"""
        return [
            entity for entity in self.entities
            if all(entity.has(comp) for comp in components)
        ]

    @property
    def get_all_entities(self):
        """get all active entities"""
        return self.entities
