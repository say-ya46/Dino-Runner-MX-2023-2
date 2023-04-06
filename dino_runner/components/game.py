import pygame

from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.bird_fly import Birds
from dino_runner.components.power_ups.powerup_manager import PowerupManager
#from threading import Timer
#from dino_runner.components.obstacles.bird_manager import ManagerBird


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.x_pos = int
        self.y_pos = 29
        self.x_pos = SCREEN_WIDTH
        
        self.running = False
        #self.dead_activate = False
        self.power_up_manager = PowerupManager()

        self.dino_dead = False

        self.points = 0

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20

        self.birds = Birds()
        self.ObstacleManager = ObstacleManager()
        
        self.x_pos_c1 = 1300
        self.y_pos_c1 = 40

        self.x_pos_c2 = 1300
        self.y_pos_c2 = 100

        self.x_pos_c = 1300
        self.y_pos_c = 200

        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()

        self.death_cont = 0

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running  :
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing = True
                self.reset()


    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()
            self.birds.update(self.player)
            self.player.update(user_input)
            self.power_up_manager.update(self.game_speed, self.points, self.player)
            self.ObstacleManager.update(self.game_speed, self.player )
            self.points += 1
            if self.points % 200 == 0:
                self.game_speed += 1
            if self.player.dino_dead:
                self.playing = False
                self.death_cont += 1
        
    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_background()
            self.power_up_manager.draw(self.screen)
            self.draw_clouds()
            self.birds.draw(self.screen)
            self.player.draw(self.screen)
            self.ObstacleManager.draw(self.screen)
            self.draw_score()
            
        else:
            self.draw_menu()
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

        self.screen.blit(CLOUD, (self.x_pos_c2, self.y_pos_c2))
        if self.x_pos_c2 <= -image_width:
            self.screen.blit(CLOUD,(image_width + self.x_pos_c2, self.y_pos_c2))
            self.x_pos_c2 = 1240
        self.x_pos_c2 -= 4

    def draw_score(self):
        score, score_rect = text_utils.get_message("points: " + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_menu(self):
        white_color = (255,255,255)
        self.screen.fill(white_color)
        if self.death_cont == 0:
            text, text_rect = text_utils.get_message("press any key to start ", 30)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message("press any key to restar ", 30)
            score, score_rect = text_utils.get_message("your score " + str(self.points), 30, height = SCREEN_HEIGHT // 2 + 50 )
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)
    def reset(self):
        self.game_speed = 20
        self.player = Dinosaur()
        self.ObstacleManager = ObstacleManager()
        self.power_up_manager = PowerupManager()
        self.points = 0


        
        