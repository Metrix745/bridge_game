'''control player behaviors'''
import pygame
from settings import SCREEN_HEIGHT, WORLD_WIDTH, RED, PLAYER_SIZE, PLAYER_SPEED, GRAVITY

class Player:
    '''player character that the user can control'''
    def __init__(self):
        self.rect = pygame.Rect(50, 50, PLAYER_SIZE, PLAYER_SIZE)
        self.vel_y = 0
        self.on_ground = False
        self.alive = True
        self.score = 0

    def update(self, platforms, enemies):
        '''update character position based on player input'''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            if self.rect.left < 0:
                self.rect.left = 0
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            if self.rect.right > WORLD_WIDTH:
                self.rect.right = WORLD_WIDTH
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = PLAYER_SPEED * -5
            self.on_ground = False

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        self.on_ground = False

        # collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # fall through platform
                if keys[pygame.K_DOWN] and platform.pass_through:
                    self.rect.top = platform.rect.bottom
                if self.vel_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.vel_y = 0
            self.on_ground = True

        # enemy handling
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if not self.on_ground and enemy.on_ground:
                    self.vel_y = -10
                    self.score += 100
                    enemies.remove(enemy)
                else:
                    self.alive = False

    def draw(self, surface, camera):
        '''reveal the character on the screen'''
        pygame.draw.rect(surface, RED, camera.apply(self.rect))
