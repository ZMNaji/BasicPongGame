import random
import pygame
import os
from game.config import *


class Ability:
    def __init__(self, screen):
        self.screen = screen
        self.img_size = 32  # 32x32 pixel
        self.path = os.path.join(os.getcwd(), "assets", "images")
        self.ability_img = self.__select_ability()
        self.position = self.__initiate_position()
        self.speed = self.__initiate_dir()

    def __select_ability(self):
        ability1 = "speed_ability"
        ability2 = "1"
        ability3 = "2"
        ability4 = "3"
        ability5 = "4"

        ability_list = [ability1, ability2, ability3, ability4, ability5]
        random_ability = random.choice(ability_list)

        img_path = os.path.join(self.path, f"{random_ability}.png")
        ability_img = pygame.image.load(img_path).convert()
        return ability_img

    def __initiate_position(self):
        range1 = (SCREEN_H / 2) + (SCREEN_H / 2)
        range2 = (SCREEN_H / 2) - (SCREEN_H / 2)
        x_pos = SCREEN_W / 2
        random_y_pos = random.randint(range2, range1)
        return (x_pos, random_y_pos)

    def __initiate_dir(self):
        directions = ["left", "right"]
        rand_dir = random.choice(directions)
        if rand_dir == "left":
            return ABILITY_SPEED * -1
        else:
            return ABILITY_SPEED

    # collision the the y axis is still broken
    def move(self, left_paddle, right_paddle):
        # note: couldn't figure why the collision with the left paddle wasn't working well
        if left_paddle.colliderect(
            self.position[0] - self.img_size + 32,
            self.position[1] - self.img_size + 32,
            2 * self.img_size,
            2 * self.img_size,
        ):
            self.speed = 0

        if right_paddle.colliderect(
            self.position[0] - self.img_size,
            self.position[1] - self.img_size,
            2 * self.img_size,
            2 * self.img_size,
        ):
            self.speed = 0

        if self.position[0] > SCREEN_W or self.position[0] < 0:
            self.speed = 0

        self.position = (self.position[0] + self.speed, self.position[1])

    def draw(self):
        self.screen.blit(self.ability_img, self.position)
