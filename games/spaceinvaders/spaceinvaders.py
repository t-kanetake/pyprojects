# project: space invaders game
# created: 12/26/2023

import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((300, 300))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(screen)



# pygame initialization
pygame.init()

# window
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# variables for game functionality
clock = pygame.time.Clock()
game = Game()

# event loop
while True:
    # exit game without throwing an error
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    # color for bg
    screen.fill((30, 30, 30))
    game.run()

    # draw bg and initialize frame rate
    pygame.display.flip()
    clock.tick(60)