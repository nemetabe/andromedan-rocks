class EventBus():
    def __init__(self):
        self.queue = []
        self.listeners = {}

    def emit(self, event):
        self.queue.append(event)

    def subscribe(self, event_type, handler):
        self.listeners.setdefault(event_type, []).append(handler)

    def flush(self):
        while self.queue[0]:
            event = self.queue.pop(0)
            for handler in self.listeners.get(type(event), []):
                handler(event)