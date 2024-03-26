import pygame as pg
import sys
from settings import RES, FPS
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
from argparse import ArgumentParser
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.ray_casting = RayCasting(self)
    
    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.player.update()
        self.ray_casting.update()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self, dimension, render_textures):
        self.screen.fill('black')
        self.object_renderer.draw(dimension, render_textures)
        self.map.draw(dimension)
        self.player.draw(dimension)
        pg.display.flip()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit() 
        
    def run(self, dimension, render_textures):
        while True:
            self.check_events()
            self.update()
            self.draw(dimension, render_textures)
        
if __name__ == '__main__':
    parser = ArgumentParser(description="Run game in 2D or 3D.")
    parser.add_argument('-d','--dimension',help="Dimensions in game.", choices=[2,3], type=int)
    parser.add_argument('-r','--render-textures',help="Whether to render textures. Only relevant in 3D.", action='store_true')
    args = vars(parser.parse_args())
    
    game = Game()
    game.run(dimension=args['dimension'],
             render_textures=args['render_textures'])