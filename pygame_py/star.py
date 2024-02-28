import random

import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.reset()

    def reset(self):
        self.x = random.randint(0, self.screen_width) - self.screen_width // 2
        self.y = random.randint(0, self.screen_height) - self.screen_height // 2
        self.z = 256
        self.color = self.settings.star_start_color

    def update(self):
        self.z -= self.settings.star_speed  
        x = self.x * 256 / self.z
        y = self.y * 256 / self.z

        if (
            self.z <= 0
            or x <= -self.screen_width // 2
            or x >= self.screen_width // 2
            or y <= -self.screen_height // 2
            or y >= self.screen_height // 2
        ):
            self.reset()

        if (
            self.color < self.settings.star_color_limit
        ):  
            self.color += self.settings.star_color_step

        if self.color >= self.settings.star_color_limit:
            self.color = self.settings.star_color_limit - 1

        x = round(self.x * 256 / self.z) + self.screen_width // 2
        y = round(self.y * 256 / self.z) + self.screen_height // 2
        pygame.draw.circle(
            self.screen,
            (self.color, self.color, self.color),
            (x, y),
            self.settings.star_radius,
        )