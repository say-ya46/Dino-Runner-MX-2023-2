from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.supper_jump import Super_jump
import random
class PowerupManager:

    POINTS = 200
    def __init__(self):
        self.power_ups = []
        self.tipos_power = 1,2,3
        self.power_elegido = int

    def update(self, game_speed, points, player):
        if len(self.power_ups) == 0 and points % self.POINTS == 0:
            self.power_elegido = random.choice(self.tipos_power)
            if self.power_elegido == 1:
                self.power_ups.append(Shield())
            elif self.power_elegido == 2:
                self.power_ups.append(Hammer())
            elif self.power_elegido == 3:
                self.power_ups.append(Super_jump())
        for power_up in self.power_ups:
            if power_up.used or power_up.rect.x < -power_up.rect.width:
                self.power_ups.pop()
            if power_up.used:
                if self.power_elegido == 1:
                    player.set_power_up(power_up)
                elif self.power_elegido == 2:
                    player.set_power_up2(power_up)
                elif self.power_elegido == 3:
                    player.set_power_up3(power_up)
            power_up.update(game_speed, player)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)