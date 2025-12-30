import time


class Clock:
    def __init__(self):
        self.last_time = None

    def reset(self):
        self.last_time = time.time()

    def tick(self):
        now = time.time()

        if self.last_time is None:
            self.last_time = now
            return 0.0

        dt = now - self.last_time
        self.last_time = now
        return dt