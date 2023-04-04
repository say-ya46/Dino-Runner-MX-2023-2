from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS

class LargeCactus(Obstacle):
    
    Y_POS_CACTUS_LARGE = 300
    #super().__init__()
    def __init__(self):
        import random
        self.image = random.choice(LARGE_CACTUS)
        super().__init__(self.image)
        self.rect.y = self.Y_POS_CACTUS_LARGE