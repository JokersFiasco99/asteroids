import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    Asteroid.containers = (asteroids, updatables, drawables)
    
    # Set AsteroidField.containers to only the updatable group
    AsteroidField.containers = (updatables,)
    
    # Create a new AsteroidField object
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatables, drawables)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    new_shot = player.shoot()
                    if new_shot:
                        shots.add(new_shot)

        screen.fill((0, 0, 0))  # Fill the entire screen with black color
        
        for sprite in updatables:
            sprite.update(dt)
        
        # Check player collision with asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()

        # Check bullet collision with asteroids
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    break  # Move to the next asteroid after destroying this one

        for sprite in drawables:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()