from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.largecactus import LargeCactus
class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        self.type_cactus = 1, 2
        self.objeto_elegido = int

    def update(self, game_speed, player):

        import random
        
        if len(self.obstacles) == 0:
            self.objeto_elegido = random.choice(self.type_cactus)
            if self.objeto_elegido == 1:
                self.obstacles.append(Cactus())
            elif self.objeto_elegido == 2:
                self.obstacles.append(LargeCactus())

        for obstacle in self.obstacles:
            if obstacle.rect.x <-  -obstacle.rect.width:
                self.obstacles.pop()
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)