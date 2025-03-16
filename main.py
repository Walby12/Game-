from pyray import *
from player import Player

init_window(960, 700, "Medieval Flappy Bird")
set_target_fps(60)

player = Player()

while not window_should_close():
    player.move()

    player.frame_timer += 1
    if player.frame_timer >= player.frame_speed:
        player.frame_timer = 0
        player.current_frame = (player.current_frame + 1) % player.frame_count  # Cycle through animation frames

    char_sprite = player.frames[player.current_frame]

    begin_drawing()
    clear_background(WHITE)

    draw_texture_pro(
        char_sprite,
        Rectangle(0, 0, char_sprite.width, char_sprite.height),
        Rectangle(int(player.player_pos[0]), int(player.player_pos[1]), char_sprite.width * 5, char_sprite.height * 5),
        Vector2(0, 0),
        0,
        WHITE
    )

    end_drawing()

for sprite in player.frames:
    unload_texture(sprite)
close_window()
