from pygame import mixer
import os
from config import *
import threading


class Music:
    def __init__(self):
        mixer.init()
        self.music_volume = MUSIC_VOLUME
        self.path = os.path.join(os.getcwd(), "assets", "music")

    def play_main_song(self):
        mixer.music.load(os.path.join(self.path, "main_menu.mp3"))
        mixer.music.set_volume(self.music_volume)
        mixer.music.play(loops=-1)

    def play_paddle_collision(self):
        mixer.music.load(os.path.join(self.path, "ball_collision2.mp3"))
        mixer.music.set_volume(self.music_volume)
        mixer.music.play()


# different way to handle music and sound effect in pygame

# class Music:
#     def __init__(self):
#         mixer.init()
#         self.music_volume = MUSIC_VOLUME
#         self.path = os.path.join(os.getcwd(), "assets", "music")

#         # Load the main menu music
#         self.main_song = mixer.Sound(os.path.join(self.path, "main_menu.mp3"))
#         self.main_song.set_volume(self.music_volume)

#         # Load the paddle collision sound
#         self.collision_sound = mixer.Sound(os.path.join(self.path, "ball_collision2.mp3"))
#         self.collision_sound.set_volume(self.music_volume)

#     def play_main_song(self):
#         self.main_song.play(loops=-1)

#     def play_paddle_collision(self):
#         self.collision_sound.play()
