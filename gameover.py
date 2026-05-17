import pygame
from constants import *

timer = pygame.time.Clock()
score = SCORE

def game_over_main(score):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dark_red = (139,0,0)
    screen.fill(dark_red)
    

    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 90)
    
    with open("highscore.txt", "r") as h:
        highscore = h.read()

    with open("highscore.txt", "r") as h:
        current_highscore_string = h.read()
        current_highscore = int(current_highscore_string.strip())
        if score > current_highscore:
            with open("highscore.txt", "w") as f:
                f.write(str(score))
                highscore = score

    


    for ammo in AMMO:
                if ammo == "Piercing":
                    score += 5
                elif ammo == "Scatter":
                    score += 2

    print("Game Over")
    print(f"Score = {score}")
    print(f"Highscore = {highscore}")
    print(f"Ammo = {AMMO}")
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
            
            
            
            
            screen.fill(dark_red)
            end_message = font.render(f"GAME OVER", False, (255,255,244))
            
            screen.blit(end_message, (SCREEN_WIDTH / 3,  9))
    
            score_surface = font.render(f"Score: {score}", False, (255, 255, 255))
        
            screen.blit(score_surface, (SCREEN_WIDTH / 3, 200))




        pygame.display.flip()
        dt = timer.tick(60) / 1000



if __name__ == "__main__":
    game_over_main()