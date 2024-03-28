import pygame as pg
import sys
from settings import RES, FPS, MOUSE_ROTATION_FLAG, KEY_ROTATION_FLAG
from level import LEVELS, Level
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
from weapon import Weapon
from object_handler import ObjectHandler
from argparse import ArgumentParser
from sound import Sound
from pathfinding import PathFinding
class Game:
    def __init__(self, level_index = 0):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.level_index = level_index
        self.new_game()
        
    def new_game(self):
        self.level = Level(self)
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.object_handler = ObjectHandler(self)
        self.ray_casting = RayCasting(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.sound.theme.play()
        self.pathfinding = PathFinding(self)
    
    def update(self, dimension, control_rotation):
        self.delta_time = self.clock.tick(FPS)
        self.player.update(dimension, control_rotation)
        self.ray_casting.update()
        self.object_handler.update()
        if dimension == 3:
            self.weapon.update()
        self.level.update()
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
        
    def draw(self, dimension, control_rotation):
        if dimension == 2:
            self.screen.fill('black')
        self.object_renderer.draw(dimension, control_rotation)
        self.map.draw(dimension)
        self.player.draw(dimension, control_rotation)
        if dimension == 2:
            [npc.draw_movement() for npc in self.object_handler.npc_list]
        if dimension == 3:
            self.weapon.draw()

        pg.display.flip()
        
    def check_events(self, control_rotation):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            self.player.single_fire_event(event, control_rotation)
        
    def run(self, dimension, control_rotation):
        while True:
            self.check_events(control_rotation)
            self.update(dimension, control_rotation)
            self.draw(dimension, control_rotation)
            if self.level.over:
                break
            
        if self.level.failed:
            self.handle_level_failed(dimension, control_rotation)
        elif self.level.completed:
            self.handle_level_completed(dimension, control_rotation)
        
    def handle_level_failed(self, dimension, control_rotation):
        self.object_renderer.draw_game_over()
        self.sound.theme.stop()
        pg.display.flip()
        pg.time.delay(2500)
        self.new_game()
        self.run(dimension, control_rotation)
        
    def handle_level_completed(self, dimension, control_rotation):
        self.object_renderer.draw_game_won()
        self.sound.theme.stop()
        pg.display.flip()
        pg.time.delay(2500)
        
        if self.level_index < len(LEVELS) - 1:
            self.level_index += 1
            self.new_game()
            self.run(dimension, control_rotation)
        
if __name__ == '__main__':
    parser = ArgumentParser(description="Run game in 2D or 3D, toggle texture rendering and controls.")
    parser.add_argument('-d','--dimension',help="Dimensions in game.", choices=[2,3], type=int)
    parser.add_argument('-ts','--turn-shoot',help="Whether to turn and shoot using left/right arrow keys and space bar, or the mouse.", choices=[MOUSE_ROTATION_FLAG, KEY_ROTATION_FLAG], default=MOUSE_ROTATION_FLAG)
    parser.add_argument('-l','--level',help="Select a level to play. Defaults to first level (1).", choices=[1, 2, 3], type=int)
    args = vars(parser.parse_args())
    
    args['level'] -= 1
    
    game = Game(args['level'])
    game.run(dimension=args['dimension'],
             control_rotation=args['turn_shoot'])