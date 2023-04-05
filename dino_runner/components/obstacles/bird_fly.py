import pygame
import random
from dino_runner.utils.constants import BIRD, DINODEAD
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Birds():

    def __init__(self):
        self.x_pos = int
        self.y_pos = 240
        self.x_pos = SCREEN_WIDTH + 500
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.x_pos
        self.bird_rect.y = self.y_pos
        self.posibles_y = [240, 150, 300, 290]
        self.step_index = 0

    def update(self,game_speed, player):
        
        self.bird_rect.x -= (game_speed)

        if self.bird_rect.colliderect(player.dino_rect):
            pygame.time.delay(300)
            player.dino_dead = True
                
        a = True
        if a:
            self.fly()



        if self.step_index >=10:
            self.step_index = 0
            

    def draw(self, screen):

        screen.blit(self.image,self.bird_rect)

        if self.bird_rect.x == 0:
            self.bird_rect.x = SCREEN_WIDTH
            self.bird_rect.y = random.choice(self.posibles_y)

    def fly(self):

        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

        #if self.x_pos == 0:
         #   self.x_pos = SCREEN_WIDTH