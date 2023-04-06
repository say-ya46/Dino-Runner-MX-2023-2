from dino_runner.utils.constants import SCREEN_WIDTH
import pygame

class Obstacle:

    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        #self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.shield:
               # player.dino_dead1()
                pygame.time.delay(300)
                player.dino_dead = True
            
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)