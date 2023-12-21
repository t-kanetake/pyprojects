# project: runner game
# created: 12/20/2023

import pygame
from sys import exit

# initialization to run pygame
pygame.init()

# window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# background and score
sky_surf = pygame.image.load("graphics/Sky.png").convert()
ground_surf = pygame.image.load("graphics/ground.png").convert()
text_surf = test_font.render("My game", False, "Black").convert()

# obstacles
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

# main game loop
while True:
    # allow to close the window without throwing an error
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # display sky
    screen.blit(sky_surf, (0, 0))

    # display ground
    screen.blit(ground_surf, (0, 300))

    #display score
    screen.blit(text_surf, (300, 50))

    # snail enemy
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)

    # player
    screen.blit(player_surf, player_rect)

    if player_rect.colliderect(snail_rect):
        print("collision")

    # display window on run
    pygame.display.update()
    clock.tick(60)