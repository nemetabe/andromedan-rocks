import time


class TimeSystem:
    def __init__(self):
        self.last_time = None
        
    def reset(self):
        self.last_time = time.time()

    def tick(self):
        now = time.time()
        dt = now - self.last_time
        self.last_time = now
        return dt