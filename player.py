from pyray import *
from raylib import *

class Player:
    def __init__(self):
        self.char_sprite = load_texture(
            r"assets\2D Pixel Dungeon Asset Pack\Character_animation\priests_idle\priest1\v1\priest1_v1_1.png")
        if self.char_sprite is None:
            print("Failed to load sprite, exiting...")
            close_window()
            exit()

        self.player_pos = [400, 300]
        self.mov_speed = 0.5

    def move(self):
        if is_key_down(KEY_W):
            self.player_pos[1] -= self.mov_speed
        if is_key_down(KEY_S):
            self.player_pos[1] += self.mov_speed
        if is_key_down(KEY_A):
            self.player_pos[0] -= self.mov_speed
        if is_key_down(KEY_D):
            self.player_pos[0] += self.mov_speed
