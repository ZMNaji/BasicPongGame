import pygame
import random
import time
from game.config import *
from game.music import Music


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
        if self.position[0] <= 0:
            score = (score[0], score[1] + 1)

        elif self.position[0] >= SCREEN_W:
            score = (score[0] + 1, score[1])

        return score
