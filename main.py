import pygame
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
from volatileasteroid import Volatile_Asteroid
from comet import Comet
from drone import Drone



#Manages game logic
def play_game(screen,font):
    

    #Resets variables upon restart
    score = SCORE
    dt = 0
    AMMO.clear()
    drones = 0

    #Group defenition
    timer = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    
    #Grouping logic
    Shot.containers = (shots,drawable,updatable)
    Piercing_Shot.containers = (shots,drawable,updatable)
    Scatter_Shot.containers = (shots,drawable,updatable)
    Player.containers = (updatable,drawable)
    Drone.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Powerup.containers = (powerups,drawable)
    Volatile_Asteroid.containers = (asteroids, updatable, drawable)
    Comet.containers = (powerups, updatable, drawable)

    #Initializes class objects
    field = AsteroidField()
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    #Manages game logic
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
          
        
        
        
        #Updates updatables
        updatable.update(dt)
        
        #Checks player/asteroid collisions and sends code to gameover
        for check_collision in asteroids:
            if check_collision.collides_with(ship): 
                if "Shield" in AMMO:
                    AMMO.remove("Shield")
                    check_collision.kill()
                    continue
                #if drones == 1:
                    check_collision.kill()
                    drone_1.kill()
                    drones -= 1
                    continue
                #elif drones == 2:
                    check_collision.kill()
                    drone_2.kill()
                    drones -= 1
                    continue
                log_event("player_hit")
                return score
            
            #Checks and deletes powerup
            for check_powerup in powerups:
                if check_powerup.collides_with(ship):
                    if check_powerup.ID == "P":
                        AMMO.append("Piercing")
                    elif check_powerup.ID == "S":
                        AMMO.append("Scatter")
                    elif check_powerup.ID == "W":
                        AMMO.append("Warp")
                    else: AMMO.append("Shield")
                    check_powerup.kill()
                    
                    #if drones == 0:
                     #drone_1 = Drone(ship.position.x + 50,ship.position.y - 50,ship)
                     #drones += 1
                    #elif drones == 1:
                     #drone_2 = Drone(ship.position.x - 50,ship.position.y - 50,ship)
                     #drones += 1
                    #elif drones == 2:
                        #pass

       #Checks collision for asteroids and shots and deletes them accordingly
        for check_asteroid in asteroids:
            for check_shot in shots:
                if check_asteroid.collides_with(check_shot):
                    
                    random_num = random.randint(0,100)
                    random_num2 = random.randint(1,4)
                    
                    check_asteroid.iframes -= dt
                    
                    if check_asteroid.iframes <= 0:
                        log_event("asteroid_shot")
                    check_asteroid.iframes = ASTEROID_IFRAMES
                    
                    #Checks if asteroid is alive and checks ID
                    if not Asteroid.alive(check_asteroid):
                        continue
                    if check_asteroid.ID == "V":
                        check_asteroid.detonate()
                        if check_asteroid.times_hit > 2:
                            random_num = 100
                        else: random_num = 0
                    else: check_asteroid.split()


                    #Generates powerups
                    if random_num > 90:
                        if random_num2 == 1:
                            Powerup(check_asteroid.position.x,check_asteroid.position.y,5,"S") 
                        elif random_num2 == 2: 
                            Powerup(check_asteroid.position.x,check_asteroid.position.y,5,"P")
                        elif random_num2 == 3:
                            Powerup(check_asteroid.position.x,check_asteroid.position.y,5,"W")
                        
                    
                    #Checks for piercing shots
                    if check_shot.radius <= 5:
                        check_shot.kill()
                    
                    #Updates score based on asteroid size
                    score += (check_asteroid.radius // 10)

        #Logs the state of the program
        log_state()
        
        #Defines the screen
        screen.fill("black")
        
        #Draws ingame sprites
        for sprite in drawable:
            sprite.draw(screen)
            
            #Draws ingame score/ammo counters
            score_surface = font.render(f"Score: {score}", False, (255, 255, 255))
            screen.blit(score_surface, (10, 10))
            ammo_surface = font.render(f"""Scatter:{AMMO.count("Scatter")} Piercing:{AMMO.count("Piercing")} Shield:{AMMO.count("Shield")} Warp:{AMMO.count("Warp")}""" , False, (255, 255, 255))
            screen.blit(ammo_surface, (875,10))
       


        #Renders sprites on the correct layer
        pygame.display.flip()
        
        #Keeps track of deltatime
        dt = timer.tick(60) / 1000

#Runs game
def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont("Arial", 24)
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"- 'Screen width: {SCREEN_WIDTH}', - 'Screen height: {SCREEN_HEIGHT}'")
    
    #Checks for highscore.txt and creates one if there are none
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
         f.write("0")
         print("Creating highscore.txt")
    
    #Game loop
    while True:
        score = play_game(screen,font)
        if score is None:
            break
        retry = game_over_main(score)
 
        #Ends game if no is selected
        if not retry:
            break

    pygame.quit
    







if __name__ == "__main__":
    main()
