# project: space invaders
# created: 12/27/2023

import pygame, sys
from player import Player
import obstacle

class Game:
    def __init__(self):
        # player setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.create_obstacle()

    def create_obstacle(self):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = col_index * self.block_size
                    y = row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)

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