import os   
import pygame
from laser import Laser

# player characteristics
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
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600
        self.lasers = pygame.sprite.Group()

# keyboard input
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()

# laser recharge
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

# borders for movement
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= 600:
            self.rect.right = 600

# align laser to shoot from player position
    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, 8, self.rect.bottom))

# call player functions
    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()