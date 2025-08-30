from constants import *
from player import *
import pygame

def main():
    pygame.init()
    # set screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # track time
    clock = pygame.time.Clock()
    dt = 0
    # instantiate player w/ mid-screen coords
    x_player = SCREEN_WIDTH / 2
    y_player = SCREEN_HEIGHT / 2
    player = Player(x_player, y_player)
    while True:
        # user able to close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # set to black to fill screen    
        color = (0,0,0)
        screen.fill(color)
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        # pause loop until 1/60 sec
        tick = clock.tick(60)
        dt = tick / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
