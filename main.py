import pygame as pg
import sys
from settings import RES, FPS, MOUSE_ROTATION_FLAG, KEY_ROTATION_FLAG
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
from weapon import Weapon
from object_handler import ObjectHandler
from argparse import ArgumentParser
from sound import Sound
class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        # self.global_trigger = False
        # self.global_event = pg.USEREVENT + 0
        # pg.time.set_timer(self.global_event, 40)
        self.new_game()
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.object_handler = ObjectHandler(self)
        self.ray_casting = RayCasting(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
    
    def update(self, dimension, control_rotation):
        self.delta_time = self.clock.tick(FPS)
        self.player.update(dimension, control_rotation)
        self.ray_casting.update()
        self.object_handler.update()
        if dimension == 3:
            self.weapon.update()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self, dimension, render_textures, control_rotation):
        if dimension == 2:
            self.screen.fill('black')
        self.object_renderer.draw(dimension, control_rotation, render_textures)
        self.map.draw(dimension)
        self.player.draw(dimension, control_rotation)
        if dimension == 2:
            [npc.draw_ray_cast() for npc in self.object_handler.npc_list]
        if dimension == 3:
            self.weapon.draw()

        pg.display.flip()
        
    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # elif event.type == self.global_event:
            #     self.global_trigger = True
            self.player.single_fire_event(event)
        
    def run(self, dimension, render_textures, control_rotation):
        while True:
            self.check_events()
            self.update(dimension, control_rotation)
            self.draw(dimension, render_textures, control_rotation)
        
if __name__ == '__main__':
    parser = ArgumentParser(description="Run game in 2D or 3D, toggle texture rendering and controls.")
    parser.add_argument('-d','--dimension',help="Dimensions in game.", choices=[2,3], type=int)
    parser.add_argument('-c','--control-rotation',help="Whether to turn using left/right arrow keys, or the mouse.", choices=[MOUSE_ROTATION_FLAG, KEY_ROTATION_FLAG], default=MOUSE_ROTATION_FLAG)
    parser.add_argument('-r','--render-textures',help="Toggle texture rendering on/off. Only relevant in 3D.", action='store_true')
    args = vars(parser.parse_args())
    
    game = Game()
    game.run(dimension=args['dimension'],
             render_textures=args['render_textures'],
             control_rotation=args['control_rotation'])