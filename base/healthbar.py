class HealthBar(Agent):
    def __init__(self, player, game, max_health, min_health):

        self.max_health = max_health
        self.min_health = min_health
        self.current_health = max_health

        self.player = player
        self.x = player.x
        self.y = player.y
        self.position = player.position

        super().__init__(self.x, self.y, self.position)

    def step(self):
        pass

    def draw_health_bar(self):
        pass

    def reset_health(self):
        self.current_health = self.max_health
