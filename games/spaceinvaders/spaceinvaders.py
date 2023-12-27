# project: space invaders
# created: 12/27/2023

import os
import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height))
        self.player = pygame.sprite.GroupSingle(player_sprite)
        

    def run(self):
        self.player.draw(screen)

if __name__ == "__main__":
    # initialize pygame
    pygame.init()

    # window
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # frame rate clock
    clock = pygame.time.Clock()

    # game class instance
    game = Game()

    # event loop
    while True:
        for event in pygame.event.get():
            # game exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # bg color
        screen.fill((30, 30, 30))

        # run game logic
        game.run()

        # draw elements in event loop
        pygame.display.flip()

        # frame rate = 60
        clock.tick(60)