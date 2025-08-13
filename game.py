import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Advanture GAME DEMO")

# Colors
WHITE = (255, 255, 255)

# Load hero image
hero_img = pygame.image.load("./resource/knight-lr.jpg").convert_alpha()  # Use convert_alpha() to keep transparency
# Scale to 10% of original size
hero_img = pygame.transform.scale(hero_img, (hero_img.get_width() // 20, hero_img.get_height() // 28))
hero_width, hero_height = hero_img.get_size()

# Load and scale background
bg_img = pygame.image.load("./resource/worldMap.jpg").convert()
bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))


# Hero position & speed
hero_x = WIDTH // 2
hero_y = HEIGHT // 2
hero_speed = 1

# Clock for controlling FPS
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                print(f"Mouse clicked at: {event.pos}")  # <-- Print position

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero_x -= hero_speed
    if keys[pygame.K_RIGHT]:
        hero_x += hero_speed
    if keys[pygame.K_UP]:
        hero_y -= hero_speed
    if keys[pygame.K_DOWN]:
        hero_y += hero_speed

    # Keep hero inside screen
    hero_x = max(0, min(WIDTH - hero_width, hero_x))
    hero_y = max(0, min(HEIGHT - hero_height, hero_y))

    # Drawing
    # screen.fill(WHITE)
    screen.blit(bg_img, (0, 0))
    screen.blit(hero_img, (hero_x, hero_y))  # Draw hero image

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
