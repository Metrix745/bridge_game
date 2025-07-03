'''control platform behaviors'''
import pygame
from settings import WHITE

class Platform:
    '''platform that player can stand on'''
    def __init__(self, x, y, width, height, color = WHITE, solid = False):
        self.rect = pygame.Rect(x, y, width, height)
        self.pass_through = not solid
        self.color = color

    def draw(self, screen, camera):
        '''show the platform on the screen'''
        pygame.draw.rect(screen, self.color, camera.apply(self.rect))
