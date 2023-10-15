import pygame
from config import *


class Paddle:
    def __init__(self, screen, paddle_type):
        self.screen = screen
        self.paddle_type = paddle_type
        self.paddle_y = LEFT_PADDLE_POSITION[1]

    def draw(self):
        if self.paddle_type == "left":
            paddle = pygame.Rect(LEFT_PADDLE_POSITION[0], self.paddle_y, PADDLE_SIZE[0], PADDLE_SIZE[1])
        else:
            paddle = pygame.Rect(RIGHT_PADDLE_POSITION[0], self.paddle_y, PADDLE_SIZE[0], PADDLE_SIZE[1])

        pygame.draw.rect(self.screen, "white", paddle)

    def update(self, direction):
        if direction == "down" and self.paddle_y <= SCREEN_H - PADDLE_SIZE[1]:
            self.paddle_y += PADDLE_SPEED
        elif direction == "up" and self.paddle_y >= 0:
            self.paddle_y -= PADDLE_SPEED


class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.position = BALL_POSITION

    def draw(self):
        pygame.draw.circle(self.screen, "white", self.position, BALL_RAD)

    def move(self):
        current_position = self.position
        self.position = (current_position[0] + BALL_SPEED, current_position[1])
