import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255),
                           self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(angle)
        new_vector_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(
            self.position[0], self.position[1], new_radius)
        new_asteroid_2 = Asteroid(
            self.position[0], self.position[1], new_radius)
        self.kill()
        new_asteroid_1.velocity = new_vector_1 * 1.2
        new_asteroid_2.velocity = new_vector_2 * 1.2
