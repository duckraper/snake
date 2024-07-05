import pygame
import os

from pygame.math import Vector2
from random import choice, randint
from settings import *
from snake import Snake
from fruit import Fruit


class Game:
    def __init__(self):
        self.running = True

        self.font = pygame.font.Font(os.path.join('assets', 'Pixeled.ttf'), 25)

        self.score = 0

        self.snake = Snake()
        self.fruit = pygame.sprite.GroupSingle(Fruit())

    def _generate_board(self):
        board = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        for i, x in enumerate(range(0, SCREEN_WIDTH, CELL_SIZE+50)):
            for j, y in enumerate(range(0, SCREEN_HEIGHT, CELL_SIZE+50)):
                if (i + j) % 2 == 0:
                    pygame.draw.rect(board, (165, 192, 111),
                                     ((x, y), (CELL_SIZE+50, CELL_SIZE+50)), 0)
                else:
                    pygame.draw.rect(board, (220, 255, 148),
                                     ((x, y), (CELL_SIZE+50, CELL_SIZE+50)), 0)

        return board

    def food_eaten(self):
        if pygame.sprite.spritecollide(self.snake.head, self.fruit, False):
            self.snake.length += 1
            self.fruit.add(Fruit())

            self.score += 1

    def self_collision(self):
        head_collision = any(
            self.snake.head.rect.colliderect(self.snake.body[i].rect)
            for i in range(len(self.snake.body) - 1)
        )

        if head_collision:
            return True

    def walls_collision(self):
        constraints = (self.snake.head.rect.right > SCREEN_WIDTH,
                       self.snake.head.rect.left < 0,
                       self.snake.head.rect.top < 0,
                       self.snake.head.rect.bottom > SCREEN_HEIGHT)

        if any(constraints):
            return True

    def restart(self):
        self.__init__()

    def game_over(self):
        caption = self.font.render(
            'Game Over', False, 'black', None)

        game_screen.blit(caption, caption.get_rect(
            center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)))

        if pygame.key.get_pressed()[pygame.K_r]:
            self.restart()

    def collisions_checker(self):
        if self.walls_collision() or self.self_collision():
            self.snake.kill()

        self.food_eaten()

    def run(self):
        self.snake.update()

        self.fruit.draw(game_screen)

        if self.snake.alive:
            self.collisions_checker()
        else:
            self.game_over()

        os.system('clear')
        print(f'score: {self.score}')
        
