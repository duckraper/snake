"""main file"""
import pygame

from game import Game
from settings import *

pygame.init()

pygame.display.set_caption("snake")

clock = pygame.time.Clock()


def main():
    """main function"""
    game = Game()

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                game.running = False
                break

        game_screen.fill((199, 231, 134))
        game.run()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
