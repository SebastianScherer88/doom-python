from sprite_object import SpriteObject, AnimatedSprite
from npc import Soldier, CacoDemon, CyberDemon
from settings import STATIC_SPRITE_PATH, ANIM_SPRITE_PATH, LEVEL_COMPLETED_DELAY
import pygame as pg

_ = False
LEVELS = [
    (
        # map
        [
            [2, 2, 2, 5, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [4, _, _, 3, 3, 1, 3, _, _, _, 1, 3, 4, _, _, 3,],
            [1, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, 3,],
            [1, _, _, _, _, _, 4, _, _, _, _, _, 4, _, _, 1,],
            [4, _, _, 3, 3, 3, 1, _, _, _, _, _, _, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [1, _, _, 5, _, _, _, 5, _, _, _, _, _, _, _, 4,],
            [1, 1, 3, 1, 3, 4, 3, 1, 3, 4, 3, 1, 1, 3, 1, 3,],
        ],
        # sprites
        [
           # static candles
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(2.8,2.5)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(2.8,5.5)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(7.2,2.5)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(7.2,5.5)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(9.8,2.5)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(12.5,5.2)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':( 6.5,1.2)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(9.5,1.2)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(12.5,1.2)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(9.5,7.8)}),
            (SpriteObject, {'path':STATIC_SPRITE_PATH + 'candlebra.png', 'pos':(12.5,7.8)}),
            # red candles in all 4 corners
            (AnimatedSprite, {'path':ANIM_SPRITE_PATH + 'red_light/0.png','pos':(1.2,7.8)}),
            (AnimatedSprite, {'path':ANIM_SPRITE_PATH + 'red_light/0.png','pos':(1.2,1.2)}),
            (AnimatedSprite, {'path':ANIM_SPRITE_PATH + 'red_light/0.png','pos':(14.8,7.8)}),
            (AnimatedSprite, {'path':ANIM_SPRITE_PATH + 'red_light/0.png','pos':(14.8,1.2)}),
            # green candles in bays
            (AnimatedSprite, {'pos':(11.8,3.2)}),
            (AnimatedSprite, {'pos':(5.8,3.5)}),
            (AnimatedSprite, {'pos':(5.8,4.5)}),
            (AnimatedSprite, {'pos':(4.2,7.8)}),
            (AnimatedSprite, {'pos':(8.2,7.8)}), 
        ],
        # npcs
        [
            (Soldier, {}),
            (Soldier,{'pos':(11.5, 4.5)}),
            (CacoDemon, {'pos':(5.5, 7.5)}),
            (CacoDemon, {'pos':(10.5, 7.5)}),
            (CyberDemon, {'pos':(13.5, 3.5)})
        ]
    ),
    (
        # map
        [
            [2, 2, 2, 5, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [4, _, _, 3, 3, 1, 3, _, _, _, 1, 3, 4, _, _, 3,],
            [1, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, 3,],
            [1, _, _, _, _, _, 4, _, _, _, _, _, 4, _, _, 1,],
            [4, _, _, 3, 3, 3, 1, _, _, _, _, _, _, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [1, _, _, 5, _, _, _, 5, _, _, _, _, _, _, _, 4,],
            [1, 1, 3, 1, 3, 4, _, _, 3, 4, _, _, _, 3, _, 3,],
            [2, 2, 2, 5, 2, 2, _, _, 2, 2, _, _, _, 2, 2, 2,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [4, _, _, 3, 3, 1, 3, _, _, _, 1, 3, 4, _, _, 3,],
            [1, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, _, _, _, 4, 2, 1, 1,],
            [4, _, _, 3, 3, 3, 1, _, _, _, _, _, _, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [1, _, _, 5, _, _, _, 5, _, _, _, _, _, _, _, 4,],
            [1, 1, 3, 1, 3, 4, 3, 1, 3, 4, 3, 1, 1, 3, 1, 3,],
        ],
        # sprites
        [
            
        ],
        # npcs
        [
            (CacoDemon, {'pos':(5.5, 7.5)}),
            (CyberDemon, {'pos':(4.5, 16.5)}),
            (CyberDemon, {'pos':(10.5, 5.5)}),
            (Soldier, {'pos':(1, 10.5)}),
            (Soldier, {'pos':(4.5, 15.5)}),
            (Soldier, {'pos':(14.5, 14.5)}),
            
        ]
    ),
    (
        # map
        [
            [2, 2, 2, 5, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [4, _, _, 3, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 3, _, _, _, 1, 3, 4, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, 4, _, _, 1,],
            [4, _, _, 3, 3, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, 3, 1, _, _, _, _, _, _, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [1, _, _, 5, _, _, _, 5, 1, 1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 4,],
            [1, 1, 3, 1, _, _, _, _, _, 3, _, _, _, _, _, _, _, _, 3, 4, _, _, 3, 4, _, _, _, 3, _, 3,],
            [2, _, _, _, _, _, _, _, _, 4, _, _, _, _, _, 2, 2, 5, 2, 2, _, _, 2, 2, _, _, _, 2, 2, 2,],
            [1, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [4, _, _, 3, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 3, _, _, _, 1, 3, 4, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, _, _, _, _, _, 3, _, _, 3,],
            [1, _, _, _, _, _, _, _, 1, 1, 2, 2, 4, 2, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1,],
            [4, _, _, 3, 3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3, 1, _, _, _, _, _, _, _, _, 3,],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1,],
            [1, _, _, 5, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 5, _, _, _, _, _, _, _, 4,],
            [1, 1, 3, 1, 3, 4, 3, 2, 5, 2, 2, 2, 2, 5, 2, 2, 2, 2, 1, 2, 2, 1, 3, 4, 3, 1, 1, 3, 1, 3,],
        ],
        # sprites
        [
            
        ],
        # npcs
        [
            (CacoDemon, {'pos':(4.5, 1.5)}),
            (CyberDemon, {'pos':(4.5, 6.5)}),
            (Soldier, {'pos':(10.5, 3.5)}),
            (Soldier, {'pos':(10.5, 5.5)}),
            (Soldier, {'pos':(10.5, 8.5)}),
            (CacoDemon, {'pos':(21.5, 3.5)}),
            (CyberDemon, {'pos':(21.5, 4.5)}),
            (CyberDemon, {'pos':(6.5, 14.5)}),
            (CacoDemon, {'pos':(15.5, 11.5)}),
            (CyberDemon, {'pos':(23.5, 14.5)}),
            (Soldier, {'pos':(23.5, 7.5)}),
            (Soldier, {'pos':(23.5, 10.5)}),
            (CyberDemon, {'pos':(26.5, 16.5)}),
        ]        
    )
]

class Level:
    def __init__(self, game):
        
        self.game = game
        self.index = game.level_index
        
        level_map, level_sprite_specs, level_npc_specs = LEVELS[self.index]
        self.map = level_map
        self.sprite_specs = level_sprite_specs
        self.npc_specs = level_npc_specs
        
        self.over = False
        self.completed_time = 0
        
    @property
    def completed(self):
        return all([not npc.alive for npc in self.game.object_handler.npc_list])
    
    @property
    def failed(self):
        return not self.game.player.alive
    
    def check_over(self):
        if not self.completed_time and self.completed:
            self.completed_time = pg.time.get_ticks()
        
        time_now = pg.time.get_ticks()
        
        if self.failed or (self.completed and time_now - self.completed_time > LEVEL_COMPLETED_DELAY):
            self.over = True
    
    def update(self):
        self.check_over()