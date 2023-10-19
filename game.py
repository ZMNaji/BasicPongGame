import pygame
import sys
import os
from config import *
from objects import Paddle, Ball, Clock, Score
from music import Music


class Game:
    def __init__(self):
        self.screen = None
        self.clock = None
        self.ball_count = 1
        self.score = (0, 0)
        self.__init_game_settings()

        self.left_paddle = Paddle(self.screen, "left")
        self.right_paddle = Paddle(self.screen, "right")
        self.ball = Ball(self.screen, self.ball_count)
        self.timer = Clock(self.screen)
        self.score_text = Score(self.screen)

    def __init_game_settings(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pong Game")
        main_menu_music = Music().play_main_song()

    def __listen_to_key_press(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.right_paddle.update("up")

        if keys[pygame.K_DOWN]:
            self.right_paddle.update("down")

        if keys[pygame.K_w]:
            self.left_paddle.update("up")

        if keys[pygame.K_s]:
            self.left_paddle.update("down")

    def start_game(self):
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    sys.exit()

            self.screen.fill(MAIN_BG)
            self.__listen_to_key_press()

            self.timer.show()
            self.score_text.show()
            self.score_text.update(self.score)

            self.left_paddle.draw()
            self.right_paddle.draw()
            self.ball.draw()
            self.ball.move(
                self.left_paddle.paddle_rect,
                self.right_paddle.paddle_rect,
            )

            # Takes current score and return new_score
            new_score = self.ball.update_score(self.score)
            if new_score != self.score:
                self.ball_count += 1
                self.ball = Ball(self.screen, self.ball_count)
                self.score = new_score

            self.clock.tick(FPS)
            pygame.display.update()

        pygame.quit
