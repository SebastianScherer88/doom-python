from sprite_object import AnimatedSprite
from random import randint, random, choice
from settings import HALF_WIDTH
import math
from settings import (
    MAX_DEPTH, 
    SOLDIER_ATTACK_DIST_MIN,
    SOLDIER_ATTACK_DIST_MAX,
    SOLDIER_SPEED,
    SOLDIER_SIZE,
    SOLDIER_HEALTH,
    SOLDIER_ATTACK_DAMAGE,
    SOLDIER_ACCURACY,
    CACO_DEMON_ATTACK_DIST,
    CACO_DEMON_SPEED,
    CACO_DEMON_SIZE,
    CACO_DEMON_HEALTH,
    CACO_DEMON_ATTACK_DAMAGE,
    CACO_DEMON_ACCURACY,
    CYBER_DEMON_ATTACK_DIST,
    CYBER_DEMON_SPEED,
    CYBER_DEMON_SIZE,
    CYBER_DEMON_HEALTH,
    CYBER_DEMON_ATTACK_DAMAGE,
    CYBER_DEMON_ACCURACY,
)
import pygame as pg

class NPC(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5,5.5),
                 scale=0.6,shift=0.38, animation_time=180):
        super().__init__(game,path,pos,scale,shift,animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')
        
        self.attack_dist = randint(3, 6)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.15
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False
        self.next_x, self.next_y = 0, 0
        
    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()
        
    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map
    
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy
        
    def movement(self):
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        self.next_x, self.next_y = next_pos
        
        if next_pos not in self.game.object_handler.npc_positions:
            angle = math.atan2(self.next_y + 0.5 - self.y, self.next_x + 0.5 - self.x)
            dx = math.cos(angle) * self.speed
            dy = math.sin(angle) * self.speed
            self.check_wall_collision(dx, dy)
            
    def attack(self):
        if self.animation_trigger:
            self.game.sound.npc_shot.play()
            if random() < self.accuracy:
                self.game.player.get_damage(self.attack_damage)
        
    def animate_death(self):
        if not self.alive:
            if self.animation_trigger and self.frame_counter < len(self.death_images) - 1:
                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1
        
    def animate_pain(self):
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False
        
    def check_hit_in_npc(self):
        if self.game.player.shot and self.ray_cast_value:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()
                
    def check_health(self):
        if self.health < 1:
            self.alive = False
            self.game.sound.npc_death.play()
        
    def run_logic(self):
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()
            
            if self.pain:
                self.animate_pain()
                
            elif self.ray_cast_value:
                self.player_search_trigger = True
                
                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()
                
            elif self.player_search_trigger:
                self.animate(self.walk_images)
                self.movement()
                
            else:
                self.animate(self.idle_images)
        else:
            self.animate_death()
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)
    
    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True
        
        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0
    
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
                
        ray_angle = self.theta
                
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)
        
        # horizontals
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)
        
        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a
        
        delta_depth = dy / sin_a
        dx = delta_depth * cos_a
        
        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth
        
        # verticals
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
        
        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a
        
        delta_depth = dx / cos_a
        dy = delta_depth * sin_a
        
        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth
            
        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)
        
        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False
    
    def draw_movement(self):
        pg.draw.circle(self.game.screen, 'blue', (100 * self.x, 100 * self.y), 15)
        if self.ray_cast_player_npc():
            pg.draw.line(self.game.screen, 'orange', (100 * self.game.player.x, 100 * self.game.player.y), (100 * self.x, 100 * self.y), 2)
            
        if self.next_x and self.next_y:
            pg.draw.rect(self.game.screen, 'blue', (100 * self.next_x, 100 * self.next_y, 100, 100))
            
class Soldier(NPC):
    def __init__(self, game, path='resources/sprites/npc/soldier/0.png', pos=(10.5,5.5),
                 scale=0.6,shift=0.38, animation_time=180):
        super().__init__(game,path,pos,scale,shift,animation_time)
        
        self.attack_dist = randint(SOLDIER_ATTACK_DIST_MIN, SOLDIER_ATTACK_DIST_MAX)
        self.speed = SOLDIER_SPEED
        self.size = SOLDIER_SIZE
        self.health = SOLDIER_HEALTH
        self.attack_damage = SOLDIER_ATTACK_DAMAGE
        self.accuracy = SOLDIER_ACCURACY

class CacoDemon(NPC):
    def __init__(self, game, path='resources/sprites/npc/caco_demon/0.png', pos=(10.5,5.5),
                 scale=0.6,shift=0.38, animation_time=180):
        super().__init__(game,path,pos,scale,shift,animation_time)
        
        self.attack_dist = CACO_DEMON_ATTACK_DIST
        self.speed = CACO_DEMON_SPEED
        self.size = CACO_DEMON_SIZE
        self.health = CACO_DEMON_HEALTH
        self.attack_damage = CACO_DEMON_ATTACK_DAMAGE
        self.accuracy = CACO_DEMON_ACCURACY

class CyberDemon(NPC):
    def __init__(self, game, path='resources/sprites/npc/cyber_demon/0.png', pos=(10.5,5.5),
                 scale=1,shift=0.1, animation_time=180):
        super().__init__(game,path,pos,scale,shift,animation_time)
        
        self.attack_dist = CYBER_DEMON_ATTACK_DIST
        self.speed = CYBER_DEMON_SPEED
        self.size = CYBER_DEMON_SIZE
        self.health = CYBER_DEMON_HEALTH
        self.attack_damage = CYBER_DEMON_ATTACK_DAMAGE
        self.accuracy = CYBER_DEMON_ACCURACY