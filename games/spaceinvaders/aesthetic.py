import os

current_dir = os.path.dirname(os.path.abspath(__file__))
game_dir = os.path.join(current_dir)
font_dir_path = os.path.join(game_dir, "font")
font_path = os.path.join(font_dir_path, "Pixeled.ttf")

get_font = lambda: font_path

current_dir2 = os.path.dirname(os.path.abspath(__file__))
game_dir2 = os.path.join(current_dir2)
graphics_path2 = os.path.join(game_dir2, "graphics")
crt_path = os.path.join(graphics_path2, "tv.png")

get_crt = lambda: crt_path

current_dir3 = os.path.dirname(os.path.abspath(__file__))
game_dir3 = os.path.join(current_dir3)
audio_path3 = os.path.join(game_dir3, "audio")
music_path = os.path.join(audio_path3, "music.wav")

get_music = lambda: music_path

current_dir4 = os.path.dirname(os.path.abspath(__file__))
game_dir4 = os.path.join(current_dir4)
audio_path4 = os.path.join(game_dir4, "audio")
explosion_path = os.path.join(audio_path4, "explosion.wav")

get_explosion_sfx = lambda: explosion_path

current_dir5 = os.path.dirname(os.path.abspath(__file__))
game_dir5 = os.path.join(current_dir5)
audio_path5 = os.path.join(game_dir5, "audio")
laser_path = os.path.join(audio_path5, "laser.wav")

get_laser_sfx = lambda: laser_path