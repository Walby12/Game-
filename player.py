from pyray import *
from raylib import *

class Player:
    def __init__(self):
        # Load frames for animation
        self.frame_paths = [
            r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_1.png",
            r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_2.png",
            r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_3.png",
            r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_4.png",
        ]
        self.frames = [load_texture(path) for path in self.frame_paths]
        self.frame_count = len(self.frames)

        # Animation variables
        self.current_frame = 0
        self.frame_speed = 8
        self.frame_timer = 0

        # Movement variables
        self.player_pos = [400, 300]  # Initial position
        self.mov_speed = 4  # Jump speed
        self.gravity = 0.3  # Gravity effect
        self.velocity_y = 0  # Vertical velocity
        self.is_jumping = False

    def move(self):
        if is_key_pressed(KEY_W) or is_key_pressed(KEY_SPACE):
            self.velocity_y = -7


        self.velocity_y += self.gravity
        self.player_pos[1] += self.velocity_y
