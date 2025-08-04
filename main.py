'''main file to handle running the game'''
import random
import pygame
from player import Player
from platforms import Platform
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, RED, FPS, WORLD_WIDTH, SPAWN_INTERVAL
from enemy import Enemy
from camera import Camera
from background import Background

def main():
    '''intializes and runs the game'''
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Platform Game")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 72)
    passed_time = 0

    player = Player()
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    background = Background()
    ground = Platform(0, 400, WORLD_WIDTH, 10, BLACK, True)
    platforms = [ground]
    enemies = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ED2 enemy spawn clock
        dt = clock.get_time()
        passed_time += dt

        if passed_time % (SPAWN_INTERVAL * 1000) < dt and len(enemies) < 1:
            enemies.append(Enemy(random.randint(0, WORLD_WIDTH), 0))

        player.update(platforms, enemies)

        # SD3 add in a scrolling function
        camera.update(player)

        background.update()

        screen.fill(BLACK)
        background.draw_bg(screen)
        background.draw_ground(screen)
        for platform in platforms[1:]:
            platform.draw(screen, camera)

        # ED2 add in enemies
        for enemy in enemies:
            enemy.update(platforms)
            enemy.draw(screen, camera)

        player.draw(screen, camera)

        # SD2 add a score function
        score = font.render(str(player.score), True, (255, 255, 255))
        score_text_rect = score.get_rect()
        screen.blit(score, score_text_rect)

        if not player.alive:
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    # SD2 GAME OVER TEXT
    if not player.alive:
        screen.fill(RED)
        game_end = font.render("Game Over", True, (255, 255, 255))
        game_end_text_rect = game_end.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_end, game_end_text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)

    pygame.quit()

if __name__ == "__main__":
    main()
