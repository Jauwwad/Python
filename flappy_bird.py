import pygame 
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)

# Game variables
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
flap_strength = -10

pipe_width = 70
pipe_gap = 150
pipe_speed = 5

score = 0
pipes = []


def create_pipe():
    y = random.randint(150, HEIGHT - 150)
    return [WIDTH, y - pipe_gap // 2, WIDTH, y + pipe_gap // 2]


def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, pipe_width, pipe[1]))
        pygame.draw.rect(screen, GREEN, (pipe[2], pipe[3], pipe_width, HEIGHT))


def check_collision(pipes, bird_x, bird_y):
    for pipe in pipes:
        if (bird_x + bird_radius > pipe[0] and bird_x - bird_radius < pipe[0] + pipe_width) and (
                bird_y - bird_radius < pipe[1] or bird_y + bird_radius > pipe[3]):
            return True
    if bird_y - bird_radius < 0 or bird_y + bird_radius > HEIGHT:
        return True
    return False


# Game loop
running = True
pipes.append(create_pipe())
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_strength

    # Bird movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # Pipe movement and generation
    for pipe in pipes:
        pipe[0] -= pipe_speed
        pipe[2] -= pipe_speed

    if pipes and pipes[0][0] + pipe_width < 0:
        pipes.pop(0)
        score += 1

    if not pipes or pipes[-1][0] < WIDTH // 2:
        pipes.append(create_pipe())

    # Draw bird and pipes
    pygame.draw.circle(screen, WHITE, (bird_x, bird_y), bird_radius)
    draw_pipes(pipes)

    # Check collisions
    if check_collision(pipes, bird_x, bird_y):
        running = False

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(30)

# End game
pygame.quit()
sys.exit()
