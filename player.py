from settings import PLAYER_ANGLE, PLAYER_POS, PLAYER_ROT_SPEED, PLAYER_SPEED, PLAYER_SIZE, PLAYER_SIGHT_RANGE, BOX_WIDTH, BOX_HEIGHT, PLAYER_SIZE_SCALE, HALF_WIDTH, HALF_HEIGHT, MOUSE_BORDER_LEFT, MOUSE_BORDER_RIGHT, MOUSE_MAX_REL, MOUSE_SENSITIVITY, MOUSE_BORDER_DOWN, MOUSE_BORDER_UP, MOUSE_CURSOR_SIZE, MOUSE_ROTATION_FLAG, KEY_ROTATION_FLAG
import pygame as pg
import math

class Player:
    def __init__(self,game):
        self.game = game
        self.size= PLAYER_SIZE
        self.scale = PLAYER_SIZE_SCALE
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        
    def movement(self, control_rotation):
        
        keys = pg.key.get_pressed()
        
        if control_rotation == KEY_ROTATION_FLAG:
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
                
    def update(self, dimension, control_rotation):
        self.movement(control_rotation)
        
        if control_rotation == MOUSE_ROTATION_FLAG:
            self.mouse_control(dimension)
        
    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        scale = self.scale / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy
    
    def get_drawing_circle_specs(self, dimension):
        
        x_off, y_off, scale_factor = self.game.map.get_minimap_offset_and_scale_factor(dimension)
        
        return (x_off + self.pos[0] * BOX_WIDTH * scale_factor, y_off + self.pos[1] * BOX_HEIGHT * scale_factor), int(self.size * scale_factor)
        
    def get_drawing_line_specs(self, dimension):
        
        x_off, y_off, scale_factor = self.game.map.get_minimap_offset_and_scale_factor(dimension)
        
        return (
            x_off + self.pos[0] * BOX_WIDTH * scale_factor,
            y_off + self.pos[1] * BOX_HEIGHT * scale_factor
        ), (
            x_off + (self.pos[0] * BOX_WIDTH + (PLAYER_SIGHT_RANGE * scale_factor) * self.trig_angle[0]) * scale_factor,
            y_off + (self.pos[1] * BOX_HEIGHT + (PLAYER_SIGHT_RANGE * scale_factor) * self.trig_angle[1]) * scale_factor
        )
        
    def get_drawing_mouse_cursor_specs(self,dimension):
        
        x_off, y_off, scale_factor = self.game.map.get_minimap_offset_and_scale_factor(dimension)
        
        mx, my = pg.mouse.get_pos()
        mx_map, my_map = mx / BOX_WIDTH, my / BOX_HEIGHT
        return (x_off + mx_map * BOX_WIDTH * scale_factor, y_off + my_map * BOX_HEIGHT * scale_factor), int(MOUSE_CURSOR_SIZE * scale_factor)
    
    def draw(self, dimension, control_rotation):
        drawing_line_specs = self.get_drawing_line_specs(dimension)
        pg.draw.line(self.game.screen, 'green',
                     drawing_line_specs[0], 
                     drawing_line_specs[1],
                     2)
        drawing_circle_specs = self.get_drawing_circle_specs(dimension)
        pg.draw.circle(self.game.screen, 'yellow',
                       drawing_circle_specs[0], 
                       drawing_circle_specs[1])
        
        if control_rotation == MOUSE_ROTATION_FLAG:
            drawing_mouse_cursor_specs = self.get_drawing_mouse_cursor_specs(dimension)
            pg.draw.circle(self.game.screen, 'red',
                        drawing_mouse_cursor_specs[0], 
                        drawing_mouse_cursor_specs[1])
        
        
    def mouse_control(self, dimension):
        mx, my = pg.mouse.get_pos()
        
        if dimension == 2:
            if mx < MOUSE_BORDER_LEFT:
                pg.mouse.set_pos([MOUSE_BORDER_LEFT, my])
            if mx > MOUSE_BORDER_RIGHT:
                pg.mouse.set_pos([MOUSE_BORDER_RIGHT, my])
            if my < MOUSE_BORDER_UP:
                pg.mouse.set_pos([mx, MOUSE_BORDER_UP])
            if my > MOUSE_BORDER_DOWN:
                pg.mouse.set_pos([mx, MOUSE_BORDER_DOWN])
                
            mx_map, my_map = mx / BOX_WIDTH, my / BOX_HEIGHT
            distx, disty = mx_map - self.x, my_map - self.y
            
            if distx == 0:
                pass
            else:
                if distx > 0:
                    self.angle = math.atan(disty / distx)
                elif distx < 0:
                    self.angle = math.atan(disty / distx) + math.pi
                
        elif dimension ==  3:
            if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
                pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
            self.rel = pg.mouse.get_rel()[0]
            self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
            self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time
            
        self.angle %= math.tau
    
    @property
    def trig_angle(self):
        return math.cos(self.angle), math.sin(self.angle)
    
    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)