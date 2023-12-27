import os   
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        game_dir = os.path.join(current_dir)
        graphics_path = os.path.join(game_dir, "graphics")
        image_path = os.path.join(graphics_path, "player.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraint = constraint

    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE]:
            self.shoot_laser()

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 600:
            self.rect.right = 600

    def shoot_laser(self):
        print("shoot laser")

    def update(self):
        self.get_input()
        self.constraint()