import pygame
from player import Player
from platforms import Platform
from settings import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platform Game")

    clock = pygame.time.Clock()
    
    player = Player()
    platforms = [Platform(400, 400, 200, 20)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(platforms)

        screen.fill(BLACK)
        for platform in platforms:
            platform.draw(screen)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
