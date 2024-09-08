import pygame
from constants import *

def main():
    pygame.init()

    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Fill the entire screen with black color
        pygame.display.flip()











if __name__ == "__main__":
    main()