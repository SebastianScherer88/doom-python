import math

# game settings
RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0
BOX_SIZE = BOX_WIDTH, BOX_HEIGHT = 100, 100
MOUSE_ROTATION_FLAG = 'm'
KEY_ROTATION_FLAG = 'k'
LEVEL_COMPLETED_DELAY = 2000

PLAYER_POS = 1.5 , 5
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE = 10
PLAYER_SIZE_SCALE = 60
PLAYER_SIGHT_RANGE = WIDTH
PLAYER_MAX_HEALTH = 100
PLAYER_DAMAGE_DURATION = 50
PLAYER_REGEN_INTERVAL = 1000
PLAYER_REGEN_RATE = 1
PLAYER_LIFE_ICON_RES = 100, 100
N_PLAYER_LIVES = 1

FOV = math.pi /3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

MINIMAP_SCALE = 0.12
MINIMAP_TOP_RIGHT = WIDTH - 50, 50

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT
MOUSE_BORDER_UP = BOX_HEIGHT
MOUSE_BORDER_DOWN = HEIGHT - MOUSE_BORDER_UP
MOUSE_MAX_REL = 40
MOUSE_SENSITIVITY = 0.0001
MOUSE_CURSOR_SIZE = 10

SKY_ROT_SPEED = 15
SKY_SCROLLING_RATE = 0.02
FLOOR_COLOR = 'darkgray'
MESSAGE_FONT = 'chalkduster.ttf'

STATIC_SPRITE_PATH = 'resources/sprites/static_sprites/'
ANIM_SPRITE_PATH = 'resources/sprites/animated_sprites/'

SOLDIER_ATTACK_DIST_MIN = 3
SOLDIER_ATTACK_DIST_MAX = 5
SOLDIER_SPEED = 0.03
SOLDIER_SIZE = 10
SOLDIER_HEALTH = 100
SOLDIER_ATTACK_DAMAGE = 10
SOLDIER_ACCURACY = 0.1

CACO_DEMON_ATTACK_DIST = 1
CACO_DEMON_SPEED = 0.02
CACO_DEMON_SIZE = 10
CACO_DEMON_HEALTH = 50
CACO_DEMON_ATTACK_DAMAGE = 10
CACO_DEMON_ACCURACY = 0.2

CYBER_DEMON_ATTACK_DIST = 6
CYBER_DEMON_SPEED = 0.02
CYBER_DEMON_SIZE = 10
CYBER_DEMON_HEALTH = 75
CYBER_DEMON_ATTACK_DAMAGE = 15
CYBER_DEMON_ACCURACY = 0.15