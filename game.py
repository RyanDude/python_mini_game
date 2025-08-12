import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Hero Movement")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Hero properties
hero_size = 50
hero_x = WIDTH // 2
hero_y = HEIGHT // 2
hero_speed = 5

# Clock for controlling FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_x -= hero_speed
    if keys[pygame.K_RIGHT]:
        hero_x += hero_speed
    if keys[pygame.K_UP]:
        hero_y -= hero_speed
    if keys[pygame.K_DOWN]:
        hero_y += hero_speed

    # Keep hero inside screen bounds
    hero_x = max(0, min(WIDTH - hero_size, hero_x))
    hero_y = max(0, min(HEIGHT - hero_size, hero_y))

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (hero_x, hero_y, hero_size, hero_size))
    pygame.display.flip()

    # Control FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
