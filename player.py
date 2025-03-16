import pyray as pr
import raylib as rp
import os

class Player:
    def __init__(self):
        if os.name == "nt":
            self.frame_paths = [
                r'assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_1.png',
                r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_2.png",
                r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_3.png",
                r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_4.png",
            ]
        else:
            self.frame_paths = [
                r'assets/2D Pixel Dungeon Asset Pack/Character_animation/priests_idle/priest1/v1/priest1_v1_1.png',
                r"assets/2D Pixel Dungeon Asset Pack/Character_animation/priests_idle/priest1/v1/priest1_v1_2.png",
                r"assets/2D Pixel Dungeon Asset Pack/Character_animation/priests_idle/priest1/v1/priest1_v1_3.png",
                r"assets/2D Pixel Dungeon Asset Pack/Character_animation/priests_idle/priest1/v1/priest1_v1_4.png",
            ]

        self.frames = [pr.load_texture(path) for path in self.frame_paths]
        self.frame_count = len(self.frames)

        self.current_frame = 0
        self.frame_speed = 8
        self.frame_timer = 0

        self.player_pos = [400, 300]
        self.mov_speed = 4
        self.gravity = 0.3
        self.velocity_y = 0
        self.is_jumping = False

    def move(self):
        if pr.is_key_pressed(rp.KEY_W) or pr.is_key_pressed(rp.KEY_SPACE):
            self.velocity_y = -7

        self.velocity_y += self.gravity
        self.player_pos[1] += self.velocity_y

        if self.player_pos[1] < 0:
            self.player_pos[1] = 0

        if self.player_pos[1] >= 638:
            self.player_pos[1] = 638
            if pr.is_key_pressed(rp.KEY_W) or pr.is_key_pressed(rp.KEY_SPACE):
                self.velocity_y = -7
        
        self.gravity = 0.3
