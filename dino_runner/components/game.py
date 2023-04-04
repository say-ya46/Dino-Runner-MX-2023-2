import pygame
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        
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
        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_clouds()
        self.player.draw(self.screen)
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
        