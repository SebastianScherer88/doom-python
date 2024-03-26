import pygame as pg
import sys
from settings import RES, FPS
from map import Map
from player import Player
from raycasting import RayCasting
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
        self.ray_casting = RayCasting(self)
    
    def update(self):
        self.delta_time = self.clock.tick(FPS)
        self.player.update()
        self.ray_casting.update()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self, mode):
        self.screen.fill('black')
        self.ray_casting.draw(mode)
        self.map.draw(mode)
        self.player.draw(mode)
        pg.display.flip()
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit() 
        
    def run(self, mode):
        while True:
            self.check_events()
            self.update()
            self.draw(mode)
        
if __name__ == '__main__':
    parser = ArgumentParser(description="Run game in 2D or 3D.")
    parser.add_argument('-m','--mode',help="Dimension mode to run game in.", choices=['2D','3D'])
    args = vars(parser.parse_args())
    
    game = Game()
    game.run(args['mode'])