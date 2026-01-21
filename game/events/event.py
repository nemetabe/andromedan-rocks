from abc import ABC
from time import time


class Event(ABC):
    def __init__(self, source=None):
        self.source = source
        self.timestamp = time()
