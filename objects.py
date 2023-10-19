import pygame
from config import *
import random
from music import Music
import time


class Paddle:
    def __init__(self, screen, paddle_type):
        self.screen = screen
        self.paddle_type = paddle_type
        self.paddle_y = LEFT_PADDLE_POSITION[1]
        self.paddle_rect = None

    def draw(self):
        if self.paddle_type == "left":
            paddle = pygame.Rect(LEFT_PADDLE_POSITION[0], self.paddle_y, PADDLE_SIZE[0], PADDLE_SIZE[1])
        else:
            paddle = pygame.Rect(RIGHT_PADDLE_POSITION[0], self.paddle_y, PADDLE_SIZE[0], PADDLE_SIZE[1])

        self.paddle_rect = paddle
        pygame.draw.rect(self.screen, "white", paddle)

    def update(self, direction):
        if direction == "down" and self.paddle_y <= SCREEN_H - PADDLE_SIZE[1]:
            self.paddle_y += PADDLE_SPEED
        elif direction == "up" and self.paddle_y >= 0:
            self.paddle_y -= PADDLE_SPEED


class Ball:
    def __init__(self, screen, ball_count):
        self.screen = screen
        self.ball_count = ball_count
        self.rad = BALL_RAD
        self.position = BALL_POSITION
        self.speed = BALL_SPEED
        self.__set_y_pos()
        self.__set_x_dir()

    def __set_y_pos(self):
        random_y = random.randint(self.position[1] - 40, self.position[1] + 40)
        self.position = (self.position[0], random_y)

    def __set_x_dir(self):
        if self.ball_count % 2 == 0:
            self.speed = (-self.speed[0], self.speed[1])

    def draw(self):
        pygame.draw.circle(self.screen, "white", self.position, self.rad)

    def move(self, left_paddle, right_paddle):
        new_position = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])

        if left_paddle.colliderect(self.position[0] - self.rad, self.position[1] - self.rad, 2 * self.rad, 2 * self.rad):
            if self.speed[0] < 0:
                self.speed = (-self.speed[0], self.speed[1])
                Music().play_paddle_collision()

        if right_paddle.colliderect(self.position[0] - self.rad, self.position[1] - self.rad, 2 * self.rad, 2 * self.rad):
            if self.speed[0] > 0:
                self.speed = (-self.speed[0], self.speed[1])
                Music().play_paddle_collision()

        if new_position[1] + self.rad >= SCREEN_H or new_position[1] - self.rad <= 0:
            self.speed = (self.speed[0], -self.speed[1])

        self.position = new_position

    def update_score(self, score):
        # if self.position[0] <= 0 or self.position[0] >= SCREEN_W:
        # return True
        if self.position[0] <= 0:
            score = (score[0] + 1, score[1])

        elif self.position[0] >= SCREEN_W:
            score = (score[0], score[1] + 1)

        return score


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
