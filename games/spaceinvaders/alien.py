import os
import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        game_dir = os.path.join(current_dir)
        graphics_path = os.path.join(game_dir, "graphics")
        image_path = os.path.join(graphics_path, f"{color}.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))

        if color == "red":
            self.value = 100
        elif color == "green":
            self.value = 200
        else:
            self.value = 300

    def update(self, direction):
        self.rect.x += direction

class Extra(pygame.sprite.Sprite):
    def __init__(self, side, screen_width):
        super().__init__()
        current_dir2 = os.path.dirname(os.path.abspath(__file__))
        game_dir2 = os.path.join(current_dir2)
        graphics_path2 = os.path.join(game_dir2, "graphics")
        image_path2 = os.path.join(graphics_path2, "extra.png")
        self.image = pygame.image.load(image_path2).convert_alpha()
        if side == "right":
            x = screen_width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3

        self.rect = self.image.get_rect(topleft = (x, 80))

    def update(self):
        self.rect.x += self.speed