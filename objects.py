import pygame
from config import *
import random
from music import Music


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
    def __init__(self, screen):
        self.screen = screen
        self.rad = BALL_RAD
        self.position = BALL_POSITION
        self.speed = BALL_SPEED
        self.__generate_init_y_position()

    def __generate_init_y_position(self):
        random_y = random.randint(self.position[1] - 40, self.position[1] + 40)
        self.position = (self.position[0], random_y)

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
