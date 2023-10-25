import pygame
import time
from game.config import *


class Clock:
    def __init__(self, screen):
        self.screen = screen
        self.timer = "00:00"
        self.current_time = time.time()
        self.seconds = 0
        self.minutes = 0

    def __update(self):
        if time.time() - self.current_time >= 1:
            self.current_time = time.time()
            self.seconds += 1

            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1

            if self.seconds < 10 and self.minutes < 10:
                self.timer = f"0{self.minutes}:0{self.seconds}"
            elif self.seconds < 10:
                self.timer = f"{self.minutes}:0{self.seconds}"
            elif self.minutes < 10:
                self.timer = f"0{self.minutes}:{self.seconds}"
            else:
                self.timer = f"{self.minutes}:{self.seconds}"

    def show(self):
        font = pygame.font.Font("freesansbold.ttf", CLOCK_TEXT_SIZE)
        text = font.render(self.timer, True, CLOCK_TEXT_COLOR, MAIN_BG)
        textRect = text.get_rect()
        textRect.center = (SCREEN_W / 2, SCREEN_H - CLOCK_TEXT_SIZE)
        self.screen.blit(text, textRect)

        self.__update()


class Score:
    def __init__(self, screen):
        self.screen = screen
        self.right_score = 0
        self.left_score = 0
        self.score = "0 - 0"

    def show(self):
        font = pygame.font.Font("freesansbold.ttf", SCORE_TEXT_SIZE)
        text = font.render(self.score, True, SCORE_TEXT_COLOR, MAIN_BG)
        textRect = text.get_rect()
        textRect.center = (SCREEN_W / 2, CLOCK_TEXT_SIZE)
        self.screen.blit(text, textRect)

    # side: left, right
    # update score based on winner side
    def update(self, score):
        self.left_score = score[0]
        self.right_score = score[1]
        self.score = f"{self.left_score} - {self.right_score}"
