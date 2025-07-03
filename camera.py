'''handle the camera behavior'''
import pygame
from settings import WORLD_WIDTH, SCREEN_HEIGHT

class Camera:
    '''camera to follow player movements'''
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, target_rect):
        '''Offset the target rect by the camera's position'''
        return target_rect.move(-self.camera.x, -self.camera.y)

    def update(self, target):
        '''keep the camera focused on the player'''
        # Center the camera on the player
        x = target.rect.centerx - self.width // 2
        y = target.rect.centery - self.height // 2

        # Clamp the camera so it doesn't show beyond the world
        x = max(0, min(x, WORLD_WIDTH - self.width))
        y = max(0, min(y, SCREEN_HEIGHT - self.height))

        self.camera.x = x
        self.camera.y = y
