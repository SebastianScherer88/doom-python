from settings import PLAYER_ANGLE, PLAYER_POS, PLAYER_ROT_SPEED, PLAYER_SPEED, PLAYER_SIZE, PLAYER_SIGHT_RANGE, BOX_WIDTH, BOX_HEIGHT, WIDTH, HEIGHT, MINIMAP_POS, MINIMAP_SCALE
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.size= PLAYER_SIZE
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        
    def movement(self):
        
        keys = pg.key.get_pressed()
        
        # player angle
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
        
        # player move
        dx, dy = 0, 0
        d_mag = PLAYER_SPEED * self.game.delta_time
        sin_a = self.trig_angle[1]
        cos_a = self.trig_angle[0]
        d_sin = d_mag * sin_a
        d_cos = d_mag * cos_a
        
        if keys[pg.K_w]:
            dx += d_cos
            dy += d_sin
        if keys[pg.K_a]:
            dx += d_sin
            dy += -d_cos
        if keys[pg.K_s]:
            dx += -d_cos
            dy += -d_sin
        if keys[pg.K_d]:
            dx += -d_sin
            dy += d_cos
                
        self.check_wall_collision(dx, dy)
                
    def update(self):
        self.movement()
        
    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.pos[0] + dx), int(self.pos[1])):
            self.x += dx
        if self.check_wall(int(self.pos[0]), int(self.pos[1] + dy)):
            self.y += dy
    
    def get_drawing_circle_specs(self, mode):
        
        x_off, y_off, scale_factor = self.game.map.get_minimap_offset_and_scale_factor(mode)
        
        return (x_off + self.pos[0] * BOX_WIDTH * scale_factor, y_off + self.pos[1] * BOX_HEIGHT * scale_factor), int(self.size * scale_factor)
        
    def get_drawing_line_specs(self, mode):
        
        x_off, y_off, scale_factor = self.game.map.get_minimap_offset_and_scale_factor(mode)
        
        return (
            x_off + self.pos[0] * BOX_WIDTH * scale_factor,
            y_off + self.pos[1] * BOX_HEIGHT * scale_factor
        ), (
            x_off + (self.pos[0] * BOX_WIDTH + (PLAYER_SIGHT_RANGE * scale_factor) * self.trig_angle[0]) * scale_factor,
            y_off + (self.pos[1] * BOX_HEIGHT + (PLAYER_SIGHT_RANGE * scale_factor) * self.trig_angle[1]) * scale_factor
        )
    
    def draw(self, mode):
        drawing_line_specs = self.get_drawing_line_specs(mode)
        pg.draw.line(self.game.screen, 'green',
                     drawing_line_specs[0], 
                     drawing_line_specs[1],
                     2)
        drawing_circle_specs = self.get_drawing_circle_specs(mode)
        pg.draw.circle(self.game.screen, 'yellow',
                       drawing_circle_specs[0], 
                       drawing_circle_specs[1])
    
    @property
    def trig_angle(self):
        return math.cos(self.angle), math.sin(self.angle)
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)