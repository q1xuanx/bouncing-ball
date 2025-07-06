import pygame
import pygame.display
import random


def random_target():
    margin = 30
    return pygame.Vector2(
        random.randint(margin, screen.get_width() - margin),
        random.randint(margin, screen.get_height() - margin)
    )


pygame.init()
pygame.font.init()

font = pygame.font.SysFont(None, 25)

screen = pygame.display.set_mode(
    size=(640, 640)
)

running = True
clock = pygame.time.Clock()
circle_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
direction = pygame.Vector2(1, 0)
speed = 299  # 100 pixels/s

segments = [circle_pos.copy()]
max_length = 50
dt = 1
score = 1
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    circle_pos += direction * speed * dt

    if (
        circle_pos.x < 0 or circle_pos.x > screen.get_width()
        or circle_pos.y < 0 or circle_pos.y > screen.get_height()
    ):
        target_pos = random_target()
        direction = (target_pos - circle_pos).normalize()
        score += 1

    segments.append(circle_pos)
    if len(segments) > max_length:
        segments.pop(0)

    screen.fill('black')

    for segment in segments:
        pygame.draw.circle(screen, 'green', segment, 20)

    score_text = font.render(f'Score: {score}', True, (255, 241, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    # Limit fps to 60
    dt = clock.tick(240) / 1000

pygame.quit()
