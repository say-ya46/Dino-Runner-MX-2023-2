import pygame
import random

from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, DINOSTART, DINODEAD, HEART, RISE
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.bird_fly import Birds
from dino_runner.components.power_ups.powerup_manager import PowerupManager

pygame.mixer.init()

jump = pygame.mixer.Sound('dino_runner/assets/sounds/jump_normal.wav')
deadS = pygame.mixer.Sound('dino_runner/assets/sounds/dead.wav')
sound_game = pygame.mixer.Sound('dino_runner/assets/sounds/game_sound.wav')
buff = pygame.mixer.Sound('dino_runner/assets/sounds/power_up_rise.wav')
menu = pygame.mixer.Sound('dino_runner/assets/sounds/sound_menu.wav')

menu.play()


#from dino_runner.components.obstacles.bird_manager import ManagerBird


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)

        self.x_pos = int
        self.y_pos = 29
        self.x_pos = SCREEN_WIDTH
        self.contadorR = 20
        
        self.running = False
        
        self.obstacle = Obstacle

        self.power_up_manager = PowerupManager()

        self.dino_dead = False

        self.points = 0
        self.activate_draw_rise = False

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
        while self.running:
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
                menu.stop()
                sound_game.play()
                self.playing = True
                self.reset()


    def update(self):
        if self.playing:
            user_input = pygame.key.get_pressed()

            self.birds.update(self.player)
            self.player.update(user_input)
            self.support_rise()

            if self.points > 0:
                self.power_up_manager.update(self.game_speed, self.points, self.player)

            self.ObstacleManager.update(self.game_speed, self.player)
            self.points += 1

            if self.points % 300 == 0:
                self.player.activate_support = True
            
            if self.player.available_life <= 0:
                sound_game.stop()
                deadS.play()
                menu.play()
                self.player.dino_dead = True

            if self.points % 200 == 0:
                self.game_speed += 1
            if self.player.dino_dead:
                self.playing = False
                self.death_cont += 1
        
    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            self.draw_rise()
            #no funcional
            #if self.player.hammerused == True:
             #   self.draw_attack()

            self.draw_background()
            if self.points > 0:
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

#no funcional el ataque del hammer
    #def draw_attack(self):
     #   image = HAMMER
      #  xpos = self.player.dino_rect.x
       # ypos = self.player.dino_rect.y
        #self.screen.blit(HAMMER, (xpos, ypos))
        
        #rect_hammer = image.get_rect()
        #if rect_hammer.colliderect(self.obstacle.rect1):
         #   self.player.hammer_colisioned = True
        #rect_hammer.x += self.game_speed

    def support_rise(self):
        if self.player.activate_support:
            buffs = 1,2,3
            buff_select = random.choice(buffs)
            if buff_select == 1:
                self.player.available_life += 20
            elif buff_select == 2:
                self.game_speed -= 1
            elif buff_select == 3:
                self.points += 50
            self.player.activate_support = False
            buff.play()
            #self.activate_draw_rise = True

    def draw_rise(self):
        
        if self.activate_draw_rise:

            image = RISE
            rise_rect = image.get_rect()
            rise_rect.x = 150
            rise_rect.y = 130
            self.screen.blit(image, rise_rect)

            if rise_rect.x <= -rise_rect.x:
                self.activate_draw_rise = False

            rise_rect.x -= 10

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
        image = HEART
        heart_rect = image.get_rect()
        heart_rect.x = 190
        heart_rect.y = 5
        self.screen.blit(image, heart_rect)

        lifes = self.player.available_life
        life, life_rect = text_utils.get_message("vida restante: " + str(lifes) + "%", 20, 100, 20)
        self.screen.blit(life, life_rect)
        
        score, score_rect = text_utils.get_message("points: " + str(self.points).zfill(7), 20, 1000, 40)
        self.screen.blit(score, score_rect)

        birds, birds_rect = text_utils.get_message("sum of birds " + str(self.birds.bird_points), 20, 1000, 70)
        self.screen.blit(birds, birds_rect)

        obstacles, obstacles_rect = text_utils.get_message("sum of obstacles " + str(self.ObstacleManager.obstacles_points), 20, 1000, 90)
        self.screen.blit(obstacles, obstacles_rect)
    def draw_menu(self):
        white_color = (255,255,255)
        self.screen.fill(white_color)
        
        if self.death_cont == 0:
            
            image = DINOSTART[0]
            start_rect = image.get_rect()
            start_rect.x = 500
            start_rect.y = 130
            self.screen.blit(image, start_rect)

            text, text_rect = text_utils.get_message("press any key to start ", 30)
            self.screen.blit(text, text_rect)
        else:
            image = DINODEAD[0]
            dead_rect = image.get_rect()
            dead_rect.x = 500
            dead_rect.y = 130
            self.screen.blit(image, dead_rect)


            tip, tip_rect = text_utils.get_message("pro tip " +  "JUMP", 20, 550, 100)
            self.screen.blit(tip, tip_rect)

            text, text_rect = text_utils.get_message("press any key to restart ", 30)
            score, score_rect = text_utils.get_message("your score " + str(self.points).zfill(7), 30, height = SCREEN_HEIGHT // 2 + 50 )
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)

            death, death_rect = text_utils.get_message("cantidad de veces jugadas " + str(self.death_cont), 20, height =SCREEN_HEIGHT // 2 + 80 )
            self.screen.blit(death, death_rect)


    def reset(self):
        self.player.available_life = 3
        self.game_speed = 20
        self.player.activate_support = False
        self.player = Dinosaur()
        self.birds = Birds()
        self.ObstacleManager = ObstacleManager()
        self.power_up_manager = PowerupManager()
        self.points = 0