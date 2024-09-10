from circleshape import CircleShape
import pygame
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import math

class Player(CircleShape):
    def __init__(self, x: int, y: int, radius):
        super().__init__(x, y, radius)
        self.rotation = 0  # Start pointing up
        self.shoot_timer = 0  # New timer variable

    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)
        right = forward.rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Invert dt for left rotation
        if keys[pygame.K_d]:
            self.rotate(dt)  # Right rotation
        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward
        
        # Decrease the shoot timer
        self.shoot_timer = max(0, self.shoot_timer - dt)

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return None  # Can't shoot yet
        
        # Reset the timer
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        # Calculate the position of the shot at the tip of the spaceship
        forward = pygame.Vector2(0, -1).rotate(-self.rotation)
        shot_pos = self.position + forward * self.radius
        
        # Calculate the velocity of the shot
        shot_velocity = forward * PLAYER_SHOOT_SPEED
        
        return Shot(shot_pos.x, shot_pos.y, shot_velocity)