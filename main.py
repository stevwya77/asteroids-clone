from constants import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *
import pygame
import sys


def main():
    pygame.init()
    
    # set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # track time
    clock = pygame.time.Clock()
    dt = 0

    # game element containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # instantiate player w/ mid-screen coords
    x_player = SCREEN_WIDTH / 2
    y_player = SCREEN_HEIGHT / 2
    player = Player(x_player, y_player)
    asteroid_field = AsteroidField()
    
    while True: 
        # user able to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # set to black to fill screen    
        color = (0,0,0)
        screen.fill(color)
        
        # draw shapes
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)

        # check for collisions & exit if true
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                sys.exit("Game Over!")
            for shot in shots:
                if shot.is_collision(asteroid):
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        
        # pause loop until 1/60 sec
        tick = clock.tick(60)
        dt = tick / 1000

if __name__ == "__main__":
    main()
