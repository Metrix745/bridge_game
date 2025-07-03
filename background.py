import os
import pygame
from settings import *

# BD3
BACKGROUND_DIR = r"bridge_game\Parallax"
SPEED = 2

class Background:
    def __init__(self):
        self.scroll = 0

        self.ground_image = pygame.image.load(os.path.join(BACKGROUND_DIR,
                                                           "ground.png")).convert_alpha()
        self.ground_width = self.ground_image.get_width()
        self.ground_height = self.ground_image.get_height()

        self.bg_images = []
        for i in range(1, 6):
            bg_image = pygame.image.load(os.path.join(BACKGROUND_DIR,
                                                      f"plx-{i}.png")).convert_alpha()
            self.bg_images.append(bg_image)
        self.bg_width = self.bg_images[0].get_width()

    def draw_bg(self, screen):
        for x in range(5):
            speed = 1
            for i in self.bg_images:
                screen.blit(i, ((x * self.bg_width) - self.scroll * speed, 0))
                speed += 0.2

    def draw_ground(self, screen):
        for x in range(15):
            screen.blit(self.ground_image,
                        ((x * self.ground_width) - self.scroll * 2.5,
                         SCREEN_HEIGHT - self.ground_height))

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.scroll > 0:
            self.scroll -= SPEED
        if key[pygame.K_RIGHT] and self.scroll < (WORLD_WIDTH * SCROLL_SPEED / PLAYER_SPEED):
            self.scroll += SPEED
