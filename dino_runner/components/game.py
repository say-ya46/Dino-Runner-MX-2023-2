import pygame
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.bird_fly import Birds
from dino_runner.components.power_ups.powerup_manager import Power_up_Manager
#from threading import Timer
#from dino_runner.components.obstacles.bird_manager import ManagerBird


class Game:
    def __init__(self):
        self.x_pos = int
        self.y_pos = 29
        self.x_pos = SCREEN_WIDTH
        
        #self.dead_activate = False
        self.power_up_manager = Power_up_Manager()

        self.dino_dead = False

        self.points = 0

        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20

        self.birds = Birds()
        self.ObstacleManager = ObstacleManager()
        
        self.x_pos_c1 = 1300
        self.y_pos_c1 = 40

        self.x_pos_c = 1300
        self.y_pos_c = 200

        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.birds.update(self.game_speed, self.player)
        self.player.update(user_input)
        self.power_up_manager.update(self.game_speed, self.points, self.player)
        self.ObstacleManager.update(self.game_speed, self.player )
        if self.player.dino_dead or self.dino_dead:
            self.playing = False
        self.points += 1
    def draw_dead(self):
        self.player.dead(self.screen)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.power_up_manager.draw()
        self.draw_clouds()
        self.birds.draw(self.screen)
        self.player.draw(self.screen)
        self.ObstacleManager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_clouds(self):
        
        image_width = CLOUD.get_width()
        
        self.screen.blit(CLOUD, (self.x_pos_c, self.y_pos_c))
        self.screen.blit(CLOUD,(image_width + self.x_pos_c, self.y_pos_c))
        if self.x_pos_c <= -image_width:
            self.screen.blit(CLOUD,(image_width + self.x_pos_c, self.y_pos_c))
            self.x_pos_c = 1240
        self.x_pos_c -= 10

        self.screen.blit(CLOUD, (self.x_pos_c1, self.y_pos_c1))
        if self.x_pos_c1 <= -image_width:
            self.screen.blit(CLOUD,(image_width + self.x_pos_c1, self.y_pos_c1))
            self.x_pos_c1 = 1240
        self.x_pos_c1 -= 15