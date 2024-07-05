import pygame
from pygame.math import Vector2

SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
CELL_SIZE = SCREEN_WIDTH // 20
#pantalla principal del juego
game_screen = pygame.display.set_mode(SCREEN_SIZE)

DIRECTIONS = {
    'right': Vector2(1, 0),
    'left': Vector2(-1, 0),
    'up': Vector2(0, -1),
    'down': Vector2(0, 1)
}

# no
