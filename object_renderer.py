import pygame as pg
import math
from settings import TEXTURE_SIZE, BOX_WIDTH, BOX_HEIGHT, MESSAGE_FONT, RES, WIDTH, HALF_HEIGHT, HALF_WIDTH, KEY_ROTATION_FLAG, MOUSE_ROTATION_FLAG, SKY_SCROLLING_RATE, SKY_ROT_SPEED, FLOOR_COLOR

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_offset = 0
        self.sky_texture = self.get_texture('resources/textures/sky.png',res=(WIDTH, HALF_HEIGHT))
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', RES)
        self.digit_size = 90
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2) for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))
        self.game_over_screen = self.get_texture(path='resources/textures/game_over.png',res=RES)
        self.game_won_screen = self.get_texture(path='resources/textures/win.png',res=RES)
        self.message_font = pg.font.SysFont(MESSAGE_FONT, 85)
        
    def player_damage(self):
        self.screen.blit(self.blood_screen, (0 ,0))
        
    def draw_player_health(self):
        if self.game.player.alive:
            health = str(self.game.player.health)
            for i, char in enumerate(health):
                self.screen.blit(self.digits[char], (i * self.digit_size, 0))
            self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size, 0))
        
    def draw_background(self, control_rotation):
        # sky
        if control_rotation == KEY_ROTATION_FLAG:            
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.sky_offset -= SKY_ROT_SPEED * SKY_SCROLLING_RATE * self.game.delta_time
            if keys[pg.K_RIGHT]:
                self.sky_offset += SKY_ROT_SPEED * SKY_SCROLLING_RATE * self.game.delta_time            
            
        elif control_rotation == MOUSE_ROTATION_FLAG:
            self.sky_offset += self.game.player.rel * SKY_SCROLLING_RATE * self.game.delta_time
            
        self.sky_offset %= WIDTH
        self.screen.blit(self.sky_texture, (WIDTH - self.sky_offset,0))
        self.screen.blit(self.sky_texture, (-self.sky_offset,0))
        
        # floor
        pg.draw.rect(self.game.screen,FLOOR_COLOR,(0,HALF_HEIGHT,WIDTH, HALF_HEIGHT))
        
    def draw_level_failed(self):
        
        self.screen.blit(self.game_over_screen, (0, 0))
        
        message = self.message_font.render(f'LEVEL {self.game.level.index + 1} FAILED', False, 'red')
        width = message.get_rect().width
        self.screen.blit(message, (HALF_WIDTH - width // 2, HALF_HEIGHT + 200))
        
    def draw_level_won(self):
        self.screen.blit(self.game_won_screen, (0, 0))
        
        message = self.message_font.render(f'LEVEL {self.game.level.index + 1} CLEARED', False, 'white')
        width = message.get_rect().width
        self.screen.blit(message, (HALF_WIDTH - width // 2, HALF_HEIGHT + 200))
        
    def draw(self, dimension, control_rotation):
    
        # 2D - FOV cone
        if dimension == 2:
            ox, oy = self.game.player.pos
            
            for depth, _, _, _, (cos_a, sin_a) in self.game.ray_casting.ray_casting_results:
                pg.draw.line(
                    self.game.screen, 
                    'yellow',
                    (ox * BOX_WIDTH, oy * BOX_HEIGHT),
                    ((ox + depth * cos_a) * BOX_WIDTH  , (oy + depth * sin_a) * BOX_HEIGHT),
                    2
                )
            
        # 3D - FOV
        elif dimension == 3:
            self.draw_background(control_rotation)
            # wall textures, sprites and NPCs
            self.render_game_objects()
            self.draw_player_health()
                
    def render_game_objects(self):
        list_objects = sorted(self.game.ray_casting.objects_to_render, key = lambda obj: obj[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image,pos)
        
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }