import pygame
from circleshape import *
from constants import PLAYER_RADIUS, SHOT_RADIUS, SHOT_COOLDOWN, PLAYER_SPEED, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.x = x
        self.y = y

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (250, 250, 250), self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        # w up
        if keys[pygame.K_w]:
            self.move(dt)
        # a left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # s down
        if keys[pygame.K_s]:
            self.move(-dt)
        # d right    
        if keys[pygame.K_d]:
            self.rotate(dt)
        # spacebar shoot
        if keys[pygame.K_SPACE]:
            self.timer -= dt
            if self.timer <= 0:
                self.shoot(self.radius, self.position, self.velocity)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, radius, position, velocity):
        shot = Shot(position.x, position.y, radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = SHOT_COOLDOWN
