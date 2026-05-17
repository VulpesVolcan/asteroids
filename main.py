import pygame
import sys
import random
import os
from constants import *
from logger import log_state,log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from piercingshot import Piercing_Shot
from scattershot import Scatter_Shot
from powerup import Powerup
from gameover import game_over_main

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"- 'Screen width: {SCREEN_WIDTH}', - 'Screen height: {SCREEN_HEIGHT}'")
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
         f.write("0")
         print("Creating highscore.txt")
    
    
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score = SCORE
    dt = 0

    font = pygame.font.SysFont("Arial", 24)
    timer = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    Piercing_Shot.containers = (shots,drawable,updatable)
    Scatter_Shot.containers = (shots,drawable,updatable)
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Powerup.containers = (powerups,drawable)
    field = AsteroidField()

    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        updatable.update(dt)
        

        for check_collision in asteroids:
            if check_collision.collides_with(ship):
                log_event("player_hit")
                
                game_over_main(score)
                sys.exit()
                

            for check_powerup in powerups:
                if check_powerup.collides_with(ship):
                    if check_powerup.ID == "P":
                        AMMO.append("Piercing")
                    else: AMMO.append("Scatter")
                    check_powerup.kill()
       
        for check_asteroid in asteroids:
            for check_shot in shots:
                
                if check_asteroid.collides_with(check_shot):
                    check_asteroid.iframes -= dt
                    if check_asteroid.iframes <= 0:
                        log_event("asteroid_shot")
                    check_asteroid.iframes = ASTEROID_IFRAMES
                    if Asteroid.alive(check_asteroid):
                        check_asteroid.split()
                        random_num = random.randint(0,100)
                        random_num2 = random.randint(1,2)
                        if random_num > 90:
                            if random_num2 == 1:
                                Powerup(check_asteroid.position.x,check_asteroid.position.y,5,"P") 
                            else: Powerup(check_asteroid.position.x,check_asteroid.position.y,5,"S")
                            
                    

                    if check_shot.radius <= 5:
                        check_shot.kill()
                    score += (check_asteroid.radius // 10)

        
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for sprite in drawable:
            sprite.draw(screen)
            
            score_surface = font.render(f"Score: {score}", False, (255, 255, 255))
            screen.blit(score_surface, (10, 10))
            scatter = AMMO.count("Scatter")
            piercing = AMMO.count("Piercing")
            ammo_surface = font.render(f"Scatter: {scatter}  Piercing {piercing}", False, (255, 255, 255))
            screen.blit(ammo_surface, (1050,10))
       
       
       
       
        pygame.display.flip()
        dt = timer.tick(60) / 1000

if __name__ == "__main__":
    main()
