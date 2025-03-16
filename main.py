import pyray as pr
from player import Player
import raylib as rp

pr.init_window(960, 700, "Medieval Flappy Bird")
pr.set_target_fps(60)

player = Player()

pr.clear_window_state(rp.FLAG_FULLSCREEN_MODE)

while not pr.window_should_close():
    player.move()

    player.frame_timer += 1
    if player.frame_timer >= player.frame_speed:
        player.frame_timer = 0
        player.current_frame = (player.current_frame + 1) % player.frame_count

    char_sprite = player.frames[player.current_frame]

    pr.begin_drawing()
    pr.clear_background(pr.WHITE)

    pr.draw_texture_pro(
        char_sprite,
        pr.Rectangle(0, 0, char_sprite.width, char_sprite.height),
        pr.Rectangle(int(player.player_pos[0]), int(player.player_pos[1]), char_sprite.width * 5, char_sprite.height * 5),
        pr.Vector2(0, 0),
        0,
        pr.WHITE
    )

    pr.end_drawing()

for sprite in player.frames:
    pr.unload_texture(sprite)
pr.close_window()
