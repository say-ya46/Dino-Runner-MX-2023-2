import pygame
#sonidos
pygame.mixer.init()

jump = pygame.mixer.Sound('dino_runner/assets/sounds/jump_normal.wav')


from dino_runner.utils.constants import (RUNNING,JUMPING,DUCKING, RUNNING_SHIELD, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SUPER,JUMPING_SUPER, DUCKING_SUPER,DINODEAD,
                                        DEFAULT_TYPE, SHIELD_TYPE, RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER, HAMMER_TYPE, JUMP_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH)

class Dinosaur:
    X_POS = 80
    Y_POS =310
    Y_POS_DUCK = 340

    def __init__(self):
        self.run_image = {DEFAULT_TYPE : RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, JUMP_TYPE: RUNNING_SUPER}
        self.duck_image = {DEFAULT_TYPE : DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, JUMP_TYPE: DUCKING_SUPER}
        self.jump_image = {DEFAULT_TYPE : JUMPING,SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, JUMP_TYPE: JUMPING_SUPER}
        self.type = DEFAULT_TYPE

        self.available_life = 100
        self.activate_support = False

        self.image = self.run_image[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False

        self.jump_sound = False

        self.jump_velC = 8.5
        self.jump_vel = self.jump_velC
        self.rest_jump = 0.8

        self.dino_dead = False


        self.hammer_colisioned = False
        self.hammerused = False
        self.hammer = False
        self.shield = False
        self.super_jump = False
        self.super = 4

        self.time_up_power = 0

    def update(self,user_input):
        if self.dino_dead:
            self.dead()

        if self.dino_jump:
            if self.jump_sound:
                jump.play()
                self.jump_sound = False
            self.jump(user_input)
            if self.hammer:
                self.hammer_used(user_input)

        if self.dino_duck:
            self.duck()
            if self.hammer:
                self.hammer_used(user_input)
            
        if self.dino_run:
            self.run()
            if self.hammer:
                self.hammer_used(user_input)

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.jump_sound = True
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False                        
            
        if self.step_index >= 10:
            self.step_index = 0

        if self.shield:
            time_to_show = round((self.time_up_power - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0:
                self.reset()

        elif self.hammer:
            time_to_show = round((self.time_up_power - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show < 0 or self.hammerused:                
                self.reset()

        elif self.super_jump:
            time_to_show = round((self.time_up_power - pygame.time.get_ticks()) / 1000, 2)
            self.super = 5
            self.jump_velC = 9.0
            self.rest_jump = 0.5
            if time_to_show < 0:
                self.reset()
        
    def draw(self,screen):
        screen.blit(self.image,self.dino_rect)
        
    def hammer_used(self, user_input):
        if user_input[pygame.K_SPACE]:
            self.hammerused = True

    def dead(self):
        x, y = self.dino_rect.x, self.dino_rect.y
        self.image = DINODEAD[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = x
        self.dino_rect.y = y
        self.screen.blit(self.image, self.dino_rect)

    def run(self):
        self.image = self.run_image[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1 

    def jump(self, user_input):
        self.image = self.jump_image[self.type]

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * self.super
            
            if user_input[pygame.K_DOWN]:
                self.rest_jump = 2
                self.jump_vel -= self.rest_jump
            else:
                self.rest_jump = 0.8
                self.jump_vel -= self.rest_jump

        if self.jump_vel < - self.jump_velC:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.jump_velC

    def duck(self):
        self.image = self.duck_image[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1 

    def set_power_up(self, power_up):
        if power_up.type == SHIELD_TYPE:
            self.shield = True
            self.type = SHIELD_TYPE
            self.time_up_power = power_up.time_up
            
    def set_power_up2(self, power_up):
        if power_up.type == HAMMER_TYPE:
            self.hammer = True
            self.type = HAMMER_TYPE
            self.time_up_power = power_up.time_up

    def set_power_up3(self, power_up):
        if power_up.type == JUMP_TYPE:
            self.type = JUMP_TYPE
            self.super_jump = True
            self.time_up_power = power_up.time_up

    def reset(self):
        self.type = DEFAULT_TYPE
        self.shield = False
        self.hammer = False
        self.hammerused = False
        self.super_jump = False
        self.super = 4
        self.jump_velC = 8.5
        self.rest_jump = 0.8
        self.time_up_power = 0