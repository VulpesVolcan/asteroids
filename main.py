import pygame
import sys
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"- 'Screen width: {SCREEN_WIDTH}', - 'Screen height: {SCREEN_HEIGHT}'")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    timer = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    field = AsteroidField()

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        updatable.update(dt)
        
        for check_collision in asteroids:
            if check_collision.collides_with(ship):
                log_event("player_hit")
                print("Game Over")
                sys.exit()
        
        for check_asteroid in asteroids:
            for check_shot in shots:
                if check_asteroid.collides_with(check_shot):
                    log_event("asteroid_shot")
                    check_asteroid.kill()
                    check_shot.kill()



        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()
