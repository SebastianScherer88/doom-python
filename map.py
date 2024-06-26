import pygame as pg
from settings import BOX_WIDTH, BOX_HEIGHT, MINIMAP_TOP_RIGHT, MINIMAP_SCALE, WIDTH, HEIGHT

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = game.level.map
        self.world_map = {}
        self.get_map()
        self.dimension = len(self.mini_map[0]), len(self.mini_map)
        
    def get_map(self):
        
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    
    def get_minimap_offset_and_scale_factor(self,dimension):
        
        if dimension == 2:
            x_off, y_off, scale_factor = 0, 0, 1
        elif dimension == 3:
            scale_factor = MINIMAP_SCALE
            x_off = MINIMAP_TOP_RIGHT[0] - self.dimension[0] * BOX_WIDTH * scale_factor
            y_off = MINIMAP_TOP_RIGHT[1]
            
        return x_off, y_off, scale_factor
                    
    def get_box_drawing_rects(self, dimension):
            
        x_off, y_off, scale_factor = self.get_minimap_offset_and_scale_factor(dimension)
            
        return [
            (
                x_off + pos[0] * BOX_WIDTH * scale_factor, 
                y_off + pos[1] * BOX_HEIGHT * scale_factor, 
                int(BOX_WIDTH * scale_factor), 
                int(BOX_HEIGHT * scale_factor)
            ) for pos in self.world_map
        ]
                    
    def draw(self, dimension):
        
        ox, oy = self.game.player.pos
        
        x_off, y_off, scale_factor = self.get_minimap_offset_and_scale_factor(dimension)
        
        if dimension == 3:
            # minimap background
            pg.draw.rect(self.game.screen, 'darkgray', (x_off, y_off, int(self.dimension[0] * BOX_WIDTH * scale_factor), int(self.dimension[1] * BOX_HEIGHT * scale_factor)), 0)
        
        # boxes - map in 2D, minimap in 3D
        [pg.draw.rect(self.game.screen, 'white', box_drawing_rect, 2) for box_drawing_rect in self.get_box_drawing_rects(dimension)]
                
        # fov - cone on map in 2D, cone on minimap in 3D
        for ray, (depth, _, _, _, (cos_a,sin_a)) in enumerate(self.game.ray_casting.ray_casting_results):
            pg.draw.line(
                self.game.screen, 
                'yellow',
                (x_off + ox * BOX_WIDTH * scale_factor, y_off + oy * BOX_HEIGHT * scale_factor),
                (x_off + (ox + depth * cos_a) * BOX_WIDTH * scale_factor  , y_off + (oy + depth * sin_a) * BOX_HEIGHT * scale_factor),
                2
            )