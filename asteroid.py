import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Remove this asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Small asteroid, just disappear

        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors
        new_vel1 = self.velocity.rotate(random_angle)
        new_vel2 = self.velocity.rotate(-random_angle)

        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set velocities for new asteroids
        new_asteroid1.velocity = new_vel1 * 1.2
        new_asteroid2.velocity = new_vel2 * 1.2

        # Add new asteroids to the game
        if self.containers:
            for container in self.containers:
                container.add(new_asteroid1)
                container.add(new_asteroid2)

        return [new_asteroid1, new_asteroid2]