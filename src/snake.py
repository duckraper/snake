import pygame

from pygame.math import Vector2
from settings import *
from os import system


class Snake:
    def __init__(self):
        self.alive = True
        self.length = 3

        self.body = []
        self.body.extend(self._create_body())

        self.head = self.body[-1]

        self.direction = DIRECTIONS['right']
        self.speed = 0.06

        self.move_timer = 0

    def _create_body(self):
        body = []
        pos = Vector2(5, 10)  # (100, 200)

        for _ in range(self.length):
            body.append(self.add_segment(pos * CELL_SIZE))
            pos.x += 1

        return body

    def add_segment(self, pos=None):
        if pos == None:
            pos = Vector2(self.head.rect.x + self.direction.x * CELL_SIZE,
                          self.head.rect.y + self.direction.y * CELL_SIZE)

        new_segment = BodySegment(pos)

        return new_segment

    def kill(self):
        self.alive = False
        system('clear')
        print("game over")

    def change_direction(self, new_direction):
        if DIRECTIONS[new_direction] != self.direction * -1:
            self.direction = DIRECTIONS[new_direction]

    def get_input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            self.change_direction('right')
        elif key[pygame.K_a] or key[pygame.K_LEFT]:
            self.change_direction('left')
        elif key[pygame.K_w] or key[pygame.K_UP]:
            self.change_direction('up')
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            self.change_direction('down')

    def move(self):
        if self.move_timer % 1 == 0:
            self.body.append(self.add_segment())

            if len(self.body) > self.length:
                del self.body[0]

        if self.move_timer >= 1:
            self.move_timer = 0
        else:
            self.move_timer += self.speed

    def update(self):
        if self.alive:
            self.move()
            self.get_input()

        for segment in self.body:
            segment.update()

        if self.length % 4 == 0:
            self.speed += 0.00025

        self.head = self.body[-1]


class BodySegment(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.layout = 3
        self.size = (CELL_SIZE - self.layout, CELL_SIZE - self.layout)
        self.color = (87, 101, 42)

        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(
            topleft=(pos.x, pos.y))

    def update(self):
        game_screen.blit(self.image, self.rect)
