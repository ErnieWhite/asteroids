import pygame
import constants
import random

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        left_vect = pygame.math.Vector2.rotate(self.velocity, angle)
        right_vect = pygame.math.Vector2.rotate(self.velocity, -angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        left_asteroid = Asteroid(*self.position, new_radius)
        right_asteroid = Asteroid(*self.position, new_radius)
        left_asteroid.velocity = left_vect * 1.2
        right_asteroid.velocity = right_vect * 1.2
