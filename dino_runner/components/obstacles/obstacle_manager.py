from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.largecactus import LargeCactus
import random
class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        self.type_cactus = 1, 2
        self.objeto_elegido = int
        self.obstacles_points = 0

    def update(self, game_speed, player):
        
        if len(self.obstacles) == 0:
            self.objeto_elegido = random.choice(self.type_cactus)
            if self.objeto_elegido == 1:
                self.obstacles.append(Cactus())
            elif self.objeto_elegido == 2:
                self.obstacles.append(LargeCactus())

        for obstacle in self.obstacles:
            if obstacle.rect.x <-  -obstacle.rect.width:
                self.obstacles.pop()
                self.obstacles_points += 1
            obstacle.update(game_speed, player)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)