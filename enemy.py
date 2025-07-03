'''dictates enemy behavior'''
import random
import pygame
from settings import WORLD_WIDTH, SCREEN_HEIGHT, BLUE, ENEMY_SIZE, ENEMY_SPEED, GRAVITY

class Enemy:
    '''enemy that player can interact with'''
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ENEMY_SIZE, ENEMY_SIZE)
        self.walk_left = bool(random.randint(0, 1))
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        '''update enemy position and state'''
        if self.walk_left:
            self.rect.x -= ENEMY_SPEED
            if self.rect.left < 0:
                self.rect.left = 0
                self.walk_left = not self.walk_left
        else:
            self.rect.x += ENEMY_SPEED
            if self.rect.right > WORLD_WIDTH:
                self.rect.right = WORLD_WIDTH
                self.walk_left = not self.walk_left

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

    def draw(self, surface, camera):
        '''draw the enemy on the screen'''
        pygame.draw.rect(surface, BLUE, camera.apply(self.rect))
