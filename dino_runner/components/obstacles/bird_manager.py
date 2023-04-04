from threading import Timer
from time import sleep
from dino_runner.components.obstacles.bird_fly import Birds

class ManagerBird:

    def __init__(self, t):
        self.bird_att = Birds()
        self.t = t
        #self.hFuncion = hFuncion
        self.thread = Timer(self.t, self.bird_att)
    
    def bird_attack(self, game_speed, player, screen):

        self.bird_att.update(game_speed, player)
        self.bird_att.draw(screen)
        self.thread.start()
    def start(self):
        self.thread = Timer(self.t, self.bird_attack)
        self.thread.start()
    def cancel(self):
        self.thread.cancel()


T = ManagerBird(1)
T.start()
sleep(2)