import pygame
from constants import *
from logger import log_state
from player import Player
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"- 'Screen width: {SCREEN_WIDTH}', - 'Screen height: {SCREEN_HEIGHT}'")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    timer = pygame.time.Clock()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        ship.update(dt)

        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        ship.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()
