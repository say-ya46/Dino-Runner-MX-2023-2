import pygame
import random
from dino_runner.utils.constants import BIRD
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Birds():

    def __init__(self):
        
        self.y_pos = 240
        self.x_pos = SCREEN_WIDTH #+ 400
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_speed = 28
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = self.x_pos
        self.bird_rect.y = self.y_pos
        self.posibles_y = [240, 180, 300, 200]
        self.step_index = 0
        self.bird_points = 0

    def update(self, player):
        
        self.bird_rect.x -= self.game_speed

        if self.bird_rect.colliderect(player.dino_rect):
            if not player.shield:
                pygame.time.delay(30)
                player.available_life -= 4
                
        a = True
        if a:
            self.fly()



        if self.step_index >=10:
            self.step_index = 0
            

    def draw(self, screen):

        screen.blit(self.image,self.bird_rect)

        if self.bird_rect.x < -self.bird_rect.width:
            self.bird_rect.x = SCREEN_WIDTH
            self.bird_rect.y = random.choice(self.posibles_y)
            self.bird_points += 1

    def fly(self):

        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1

        #if self.x_pos == 0:
         #   self.x_pos = SCREEN_WIDTH