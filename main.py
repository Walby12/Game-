from pyray import *
from player import Player

init_window(800, 600, "Test")

monitor_w = get_monitor_width(0)
monitor_h = get_monitor_height(0)

set_window_size(monitor_w, monitor_h)

player = Player()

toggle_fullscreen()

while not window_should_close():
    player.move()

    begin_drawing()
    clear_background(WHITE)

    if player.player_pos[0] >= monitor_w - 130:
        player.player_pos[0] = monitor_w - 130

    if player.player_pos[0] < 0 + 10 :
        player.player_pos[0] = 10

    if player.player_pos[1] >= monitor_h - 130:
        player.player_pos[1] = monitor_h - 130

    if player.player_pos[1] < 0:
        player.player_pos[1] = 0

    draw_texture_ex(player.char_sprite, (int(player.player_pos[0]), int(player.player_pos[1])),0,8, WHITE)

    end_drawing()

unload_texture(player.char_sprite)
close_window()

