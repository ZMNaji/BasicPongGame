import pygame
import sys
import os
import random
from game.config import *
from game.objects import Paddle, Ball
from game.text_objects import Clock, Score
from game.music import Music
from game.abitlies import Ability


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
        self.current_ability = None

    def __init_game_settings(self):
        pygame.init()
        self.screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pong Game")
        Music().play_main_song()

    ## FUNCTIONS THAT RUN INSIDE THE MAIN GAME LOOP ##
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

    def __handle_score_and_timer(self):
        self.timer.show()
        self.score_text.show()
        self.score_text.update(self.score)

        # Takes current score and return new_score
        new_score = self.ball.update_score(self.score)
        if new_score != self.score:
            self.ball_count += 1
            self.ball = Ball(self.screen, self.ball_count)
            self.score = new_score

    def __handle_paddles_and_ball(self):
        self.left_paddle.draw()
        self.right_paddle.draw()
        self.ball.draw()
        self.ball.move(
            self.left_paddle.paddle_rect,
            self.right_paddle.paddle_rect,
        )

    def __handle_ability(self):
        if self.current_ability is None:
            range1 = 0
            range2 = 1 * 100
            chance = random.randint(range1, range2)
            if chance == range2:
                self.current_ability = Ability(self.screen)

        if self.current_ability is not None:
            self.current_ability.draw()
            self.current_ability.move(
                self.left_paddle.paddle_rect,
                self.right_paddle.paddle_rect,
            )
            if self.current_ability.speed == 0:
                self.current_ability = None

    def start_game(self):
        is_running = True

        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                    sys.exit()

            self.screen.fill(MAIN_BG)

            self.__listen_to_key_press()
            self.__handle_score_and_timer()
            self.__handle_paddles_and_ball()
            self.__handle_ability()
            self.clock.tick(FPS)
            pygame.display.update()

        pygame.quit
