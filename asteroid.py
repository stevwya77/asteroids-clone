import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            
            # use random angle for two opposite direction split
            pos_angle = self.velocity.rotate(angle)
            neg_angle = self.velocity.rotate(-angle)
            
            # broken asteroids smaller than previous
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # create the two asteroids
            ast_one = Asteroid(self.position.x, self.position.y, new_radius)
            ast_two = Asteroid(self.position.x, self.position.y, new_radius)
            
            # set velocity based on angle
            ast_one.velocity = pos_angle * 1.2
            ast_two.velocity = neg_angle * 1.2
