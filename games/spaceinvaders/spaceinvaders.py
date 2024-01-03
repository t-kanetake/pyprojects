# project: space invaders
# created: 12/27/2023

"""this file is nested within other directories which is why the os module is used in inherited files"""

import pygame, sys
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser
from aesthetic import get_font, get_crt, get_explosion_sfx, get_laser_sfx, get_music

class Game:
    def __init__(self):
        # player setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # health & score
        player_image = self.player.sprite.get_image_path
        self.lives = 3
        self.life_surf = pygame.image.load(player_image()).convert_alpha()
        self.life_x_start_pos = screen_width - (self.life_surf.get_size()[0] * 2 + 20)
        self.score = 0
        self.font = get_font()
        self.font = pygame.font.Font(self.font, 20)
        
        # obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
        self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = screen_width / 15, y_start=480)

        # alien setup
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.alien_setup()
        self.alien_setup(rows=6, cols=8)
        self.alien_direction = 1

        # extra alien setup
        self.extra = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(400, 800)

        # audio
        bg_music = get_music()
        music = pygame.mixer.Sound(bg_music)
        music.set_volume(0.1)
        music.play(loops=-1)
        self.get_laser = get_laser_sfx()
        self.laser_sound = pygame.mixer.Sound(self.get_laser)
        self.laser_sound.set_volume(0.07)
        self.get_explosion = get_explosion_sfx()
        self.explosion_sound = pygame.mixer.Sound(self.get_explosion)
        self.explosion_sound.set_volume(0.03)

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == "x":
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, (241, 79, 80), x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, *offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)

    def alien_setup(self, rows=0, cols=0, x_distance=60, y_distance=48, x_offset=70, y_offset=100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:
                    alien_sprite = Alien("yellow", x ,y)
                elif 1 <= row_index <= 2:
                    alien_sprite = Alien("green", x, y)
                else:
                    alien_sprite = Alien("red", x, y)
                self.aliens.add(alien_sprite)

    def alien_pos_checker(self):
        all_aliens = self.aliens.sprites()
        for alien in all_aliens:
            if alien.rect.right >= screen_width:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= 0:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens:
            for alien in self.aliens.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens.sprites():
            random_alien = choice(self.aliens.sprites())
            laser_sprite = Laser(random_alien.rect.center, 6, screen_height)
            self.alien_lasers.add(laser_sprite)
            self.laser_sound.play()

    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            self.extra.add(Extra(choice(["right", "left"]), screen_width))
            self.extra_spawn_time = randint(400, 800)

    def collision_checks(self):

        # player lasers
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                # obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()
                
                # alien collision
                aliens_hit = pygame.sprite.spritecollide(laser, self.aliens, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.value
                    laser.kill()
                    self.explosion_sound.play()
                    
                # extra collision
                if pygame.sprite.spritecollide(laser, self.extra, True):
                    laser.kill()
                    self.score += 500

        # alien laser
        if self.alien_lasers:
            for laser in self.alien_lasers:                
                # obstacle collision
                if pygame.sprite.spritecollide(laser, self.blocks, True):
                    laser.kill()
                if pygame.sprite.spritecollide(laser, self.player, False):
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        pygame.quit()
                        sys.exit()

        # aliens
        if self.aliens:
            for alien in self.aliens:
                pygame.sprite.spritecollide(alien, self.blocks, True)

                if pygame.sprite.spritecollide(alien, self.player, False):
                    laser.kill()
                    pygame.quit()
                    sys.exit()

    def display_lives(self):
        for life in range(self.lives - 1):
            x = self.life_x_start_pos + (life * (self.life_surf.get_size()[0] + 10))
            screen.blit(self.life_surf, (x, 8))

    def display_score(self):
        score_surf = self.font.render(f"Score: {self.score}", False, "White")
        score_rect = score_surf.get_rect(topleft = (10, -10))
        screen.blit(score_surf, score_rect)

    def victory_message(self):
        if not self.aliens.sprites():
            victory_surf = self.font.render("You won", False, "white")
            victory_rect = victory_surf.get_rect(center = (screen_width / 2, screen_height / 2))
            screen.blit(victory_surf, victory_rect)

    def run(self):
        # call object methods to execute
        self.player.update()
        self.aliens.update(self.alien_direction)
        self.alien_pos_checker()
        self.alien_lasers.update()
        self.extra_alien_timer()
        self.extra.update()
        self.collision_checks()
        self.display_lives()
        self.display_score()
        self.victory_message()

        # draw player attributes
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)

        # draw everything else
        self.blocks.draw(screen)
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra.draw(screen)

class CRT:
    def __init__(self):
        get_tv = get_crt()
        self.tv = pygame.image.load(get_tv).convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (screen_width, screen_height))

    def crt_lines(self):
        line_height = 3
        line_amount = int(screen_height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, "black", (0, y_pos), (screen_width, y_pos), 1)

    def draw(self):
        self.tv.set_alpha(randint(75, 90))
        self.crt_lines()
        screen.blit(self.tv, (0, 0))

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

    # CRT filter
    crt = CRT()

    # alien laser timer
    alienlaser = pygame.USEREVENT + 1
    pygame.time.set_timer(alienlaser, 800)

    # event loop
    while True:
        for event in pygame.event.get():
            # game exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == alienlaser:
                game.alien_shoot()

        # bg color
        screen.fill((30, 30, 30))

        # run game logic
        game.run()

        # display CRT filter
        crt.draw()

        # draw elements in event loop
        pygame.display.flip()

        # frame rate = 60
        clock.tick(60)