import pygame as pg
from settings import BOX_WIDTH, BOX_HEIGHT, MINIMAP_POS, MINIMAP_SCALE, WIDTH, HEIGHT

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
    [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1,],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1,],
    [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1,],
    [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1,],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
    [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
        
    def get_map(self):
        
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value
                    
    def get_minimap_offset_and_scale_factor(self,mode):
        
        if mode == '2D':
            x_off, y_off, scale_factor = 0, 0, 1
        elif mode == '3D':
            x_off, y_off, scale_factor = MINIMAP_POS[0], MINIMAP_POS[1], MINIMAP_SCALE
            
        return x_off, y_off, scale_factor
                    
    def get_box_drawing_rects(self, mode):
            
        x_off, y_off, scale_factor = self.get_minimap_offset_and_scale_factor(mode)
            
        return [
            (
                x_off + pos[0] * BOX_WIDTH * scale_factor, 
                y_off + pos[1] * BOX_HEIGHT * scale_factor, 
                int(BOX_WIDTH * scale_factor), 
                int(BOX_HEIGHT * scale_factor)
            ) for pos in self.world_map
            ]
                    
    def draw(self, mode):
        
        ox, oy = self.game.player.pos
        
        x_off, y_off, scale_factor = self.get_minimap_offset_and_scale_factor(mode)
        
        if mode == '3D':
            # minimap background
            pg.draw.rect(self.game.screen, 'darkgray', (x_off, y_off, int(WIDTH * scale_factor), int(HEIGHT * scale_factor)), 0)
        
        # boxes
        [pg.draw.rect(self.game.screen, 'white', box_drawing_rect, 2) for box_drawing_rect in self.get_box_drawing_rects(mode)]
        
        # fov
        for ray, (depth, (cos_a,sin_a)) in enumerate(
            zip(
                self.game.ray_casting.depths,
                self.game.ray_casting.trig_angles
                )
            ):
            pg.draw.line(
                self.game.screen, 
                'yellow',
                (x_off + ox * BOX_WIDTH * scale_factor, y_off + oy * BOX_HEIGHT * scale_factor),
                (x_off + (ox + depth * cos_a) * BOX_WIDTH * scale_factor  , y_off + (oy + depth * sin_a) * BOX_HEIGHT * scale_factor),
                2
            )
    