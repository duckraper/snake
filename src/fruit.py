import pygame

from pygame.sprite import Sprite
from random import randint
from settings import *


class Fruit(Sprite):
    def __init__(self):
        super().__init__()

        self.layout = 10
        self.size = (CELL_SIZE - self.layout, CELL_SIZE - self.layout)

        self.image = pygame.Surface(self.size)
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=self._randomize_position())

    def _randomize_position(self):
        return (randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE + self.layout//2,
                randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE + self.layout//2)
