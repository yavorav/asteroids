import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable) # should add all instances of Asteroid class automatically to group when created
    AsteroidField.containers = (updatable)

    spaceship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        # allows for the game to be quit with the 'X' button of the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fills the screen with solid colour, black
        pygame.Surface.fill(screen, (0, 0, 0))
        # draws the player ship
        for thing in updatable:
            thing.update(dt)
        # spaceship.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_detection(spaceship):
                print("Game over!")
                sys.exit()
        # spacesS
        for thing in drawable:
            thing.draw(screen)
        # Refreshes the screen
        pygame.display.flip()
        # Limit the framerate to 60fps
        dt = clock.tick(60) / 1000
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()