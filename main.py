import pygame
import sys
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from subshot import Sub_Shot
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"- 'Screen width: {SCREEN_WIDTH}', - 'Screen height: {SCREEN_HEIGHT}'")
    pygame.init()
    pygame.font.init()

    with open("highscore.txt", "r") as h:
        highscore = h.read()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = 0
    dt = 0
    font = pygame.font.SysFont("Arial", 24)
    timer = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Sub_Shot.containers = (shots,drawable,updatable)
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
                print(f"Score = {score}")
                print(f"Highscore = {highscore}")
                sys.exit()
        
        for check_asteroid in asteroids:
            for check_shot in shots:
                if check_asteroid.collides_with(check_shot):
                    log_event("asteroid_shot")
                    check_asteroid.split()
                    if check_shot.radius == 5:
                        check_shot.kill()
                    score += (check_asteroid.radius // 10)
                    with open("highscore.txt", "r") as h:
                        current_highscore_string = h.read()
                        current_highscore = int(current_highscore_string.strip())
                        if score > current_highscore:
                            with open("highscore.txt", "w") as f:
                                f.write(str(score))
                                highscore = score
                    

        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
            score_surface = font.render(f"Score: {score}", False, (255, 255, 255))
            screen.blit(score_surface, (10, 10))
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()
