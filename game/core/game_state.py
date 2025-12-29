class GameState():
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.phase = "PLAYING"

    def on_asteroid_avoided(self, event):
        self.score += 1

    def on_asteroid_hit(self, event):
        self.lives -= 1
        if self.lives <= 0:
            self.phase = "GAME_OVER"