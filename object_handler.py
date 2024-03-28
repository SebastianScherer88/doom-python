class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_positions = []
        
        for sprite_class, sprite_kwargs in self.game.level.sprite_specs:
            sprite = sprite_class(game, **sprite_kwargs)
            self.add_sprite(sprite)
            
        for npc_class, npc_kwargs in self.game.level.npc_specs:
            npc = npc_class(game, **npc_kwargs)
            self.add_npc(npc)
        
    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.npc_positions = [npc.map_pos for npc in self.npc_list if npc.alive]
        
    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
        
    def add_npc(self, npc):
        self.npc_list.append(npc)