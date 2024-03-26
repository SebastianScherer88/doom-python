import pygame as pg
from settings import TEXTURE_SIZE, BOX_WIDTH, BOX_HEIGHT, SCALE, HALF_HEIGHT

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        
    def draw(self, dimension, render_textures):

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
        elif dimension == 3 and not render_textures:
            for ray, (depth, proj_height, _, _, _) in enumerate(self.game.ray_casting.ray_casting_results):
                color = 255 / (1 + depth ** 5 * 0.00002), 200 / (1 + depth ** 5 * 0.00002), 100 / (1 + depth ** 5 * 0.00002)
                pg.draw.rect(
                    self.game.screen, 
                    color,
                    (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height),
                    width=2
                )
        
        # 3D-render: FOV with textures
        elif dimension == 3 and render_textures:
            self.render_game_objects()
                
    def render_game_objects(self):
        list_objects = self.game.ray_casting.objects_to_render
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