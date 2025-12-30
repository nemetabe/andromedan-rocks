from abc import ABC
from .component import Component


class Entity(ABC):
    """Entity = ID + bag of components"""
    _next_id = 0
    
    def __init__(self):
        self.id = Entity._next_id
        Entity._next_id += 1
        self.components: dict[type[Component], Component] = {}
    
    def add(self, component: Component):
        self.components[type(component)] = component
        return self
    
    def get(self, component_type: type[Component]):
        return self.components.get(component_type)
    
    def has(self, component_type: type[Component]) -> bool:
        return component_type in self.components
    
    def remove(self, component_type: type[Component]):
        if component_type in self.components:
            del self.components[component_type]
