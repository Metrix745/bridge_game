import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 50, 50)
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.rect.left < 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
        if keys[pygame.K_SPACE]:
            self.vel_y = -20
            self.on_ground = False

        self.vel_y += 1
        self.rect.y += self.vel_y

        # collisions
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.vel_y > 0:
                self.rect.bottom = platform.rect.top
                self.vel_y = 0
                self.on_ground = True

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)
