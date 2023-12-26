# project: space invaders game
# created: 12/26/2023

import pygame, sys

# pygame initialization
pygame.init()

# window
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# framerate class
clock = pygame.time.Clock()

# event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    # color for bg
    screen.fill((30, 30, 30))

    pygame.display.flip()
    clock.tick(60)