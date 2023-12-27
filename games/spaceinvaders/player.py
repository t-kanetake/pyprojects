import os   
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        game_dir = os.path.join(current_dir)
        graphics_path = os.path.join(game_dir, "graphics")
        image_path = os.path.join(graphics_path, "player.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)