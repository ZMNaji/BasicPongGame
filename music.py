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
        main_song_thread = threading.Thread(target=self.__play_main_song)
        main_song_thread.start()

    def __play_main_song(self):
        mixer.music.load(os.path.join(self.path, "main_menu.mp3"))
        mixer.music.set_volume(self.music_volume)
        mixer.music.play(loops=-1)

    def play_paddle_collision(self):
        collision_sound_thread = threading.Thread(target=self.__play_collision_sound)
        collision_sound_thread.start()

    def __play_collision_sound(self):
        sound = mixer.Sound(os.path.join(self.path, "ball_collision2.mp3"))
        sound.set_volume(self.music_volume)
        sound.play()
