from sprite_object import SpriteObject, AnimatedSprite
from npc import NPC

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.static_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = []
        
        # sprite map
        # static candles
        add_sprite(SpriteObject(game, pos=(2.8,2.5)))
        add_sprite(SpriteObject(game, pos=(2.8,5.5)))
        add_sprite(SpriteObject(game, pos=(7.2,2.5)))
        add_sprite(SpriteObject(game, pos=(7.2,5.5)))
        add_sprite(SpriteObject(game, pos=(9.8,2.5)))
        add_sprite(SpriteObject(game, pos=(12.5,5.2)))
        add_sprite(SpriteObject(game, pos=( 6.5,1.2)))
        add_sprite(SpriteObject(game, pos=(9.5,1.2)))
        add_sprite(SpriteObject(game, pos=(12.5,1.2)))
        add_sprite(SpriteObject(game, pos=(9.5,7.8)))
        add_sprite(SpriteObject(game, pos=(12.5,7.8)))
        # red candles in all 4 corners
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png',pos=(1.2,7.8)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png',pos=(1.2,1.2)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png',pos=(14.8,7.8)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png',pos=(14.8,1.2)))
        # green candles in bays
        add_sprite(AnimatedSprite(game,pos=(11.8,3.2)))
        add_sprite(AnimatedSprite(game, pos=(5.8,3.5)))
        add_sprite(AnimatedSprite(game, pos=(5.8,4.5)))
        add_sprite(AnimatedSprite(game, pos=(4.2,7.8)))
        add_sprite(AnimatedSprite(game, pos=(8.2,7.8)))
        
        # npc map
        add_npc(NPC(game))
        add_npc(NPC(game, pos = (11.5, 4.5)))
        
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.npc_positions = [npc.map_pos for npc in self.npc_list if npc.alive]
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
        
    def add_npc(self, npc):
        self.npc_list.append(npc)