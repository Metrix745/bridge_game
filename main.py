'''main file to handle running the game'''
import random
import csv
import pygame
from player import Player
from platforms import Platform
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, RED, FPS, WORLD_WIDTH, SPAWN_INTERVAL, HIGH_SCORES
from enemy import Enemy
from camera import Camera
from background import Background

def main():
    '''intializes and runs the game'''
    scores = []

    with open(HIGH_SCORES, 'r', newline='', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in reader:
            scores.append((row[0], row[1]))

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

        if passed_time % (SPAWN_INTERVAL * 1000) < dt and len(enemies) < 5:
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

    done = False
    scored = True

    # If there are already 5 high scores and the player's score is less than the lowest, skip name entry
    if len(scores) >= 5 and player.score < min(int(s[1]) for s in scores):
        scored = False

    # Prompt for player name after game over
    screen.fill(BLACK)
    input_box = pygame.Rect(SCREEN_WIDTH//2, 100, 200, 50)
    text = ""
    prompt = font.render("Enter your name:", True, RED)
    prompt_rect = prompt.get_rect(center=(SCREEN_WIDTH // 2, 80))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_name = text
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill(BLACK)
        screen.blit(prompt, prompt_rect)
        txt_surface = font.render(text, True, RED)
        width = txt_surface.get_width() + 10
        input_box.w = width
        # Center the input box horizontally
        input_box.x = (SCREEN_WIDTH - input_box.w) // 2
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # pygame.draw.rect(screen, RED, input_box, 2)
        pygame.display.flip()

    # Display player name and score
    if scored:
        screen.fill(BLACK)
        player_name = text
        name_surface = font.render(f"Player: {player_name}", True, RED)
        score_surface = font.render(f"Score: {player.score}", True, RED)
        name_rect = name_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
        screen.blit(name_surface, name_rect)
        screen.blit(score_surface, score_rect)
        pygame.display.flip()
        pygame.time.wait(2000)

        # display high scores
        # Add new score to the list and sort
        scores.append((player_name, str(player.score)))
    scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)[:5]

    # Save top 5 scores back to file
    with open(HIGH_SCORES, 'w', encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter=' ', quotechar='|')
        for name, score in scores:
            writer.writerow([name, score])

    # Display top 5 high scores
    screen.fill(BLACK)
    title = font.render("High Scores", True, RED)
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 60))
    screen.blit(title, title_rect)
    for i, (name, score) in enumerate(scores):
        entry = font.render(f"{i+1}. {name}: {score}", True, (255, 255, 255))
        entry_rect = entry.get_rect(center=(SCREEN_WIDTH // 2, 140 + i * 60))
        screen.blit(entry, entry_rect)
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
