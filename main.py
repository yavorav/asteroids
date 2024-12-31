import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    spaceship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        # allows for the game to be quit with the 'X' button of the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills the screen with solid colour, black
        pygame.Surface.fill(screen, (0, 0, 0))
        # draws the player ship
        spaceship.draw(screen)
        # Refreshes the screen
        pygame.display.flip()
        # Limit the framerate to 60fps
        dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()