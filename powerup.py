import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS,LINE_WIDTH,AMMO

class Powerup(CircleShape):
    def __init__(self, x, y, radius,ID):
        super().__init__(x, y, SHOT_RADIUS)
        self.ID = ID
        self.color = "white"

    def draw(self,screen):
        if self.ID == "S":
            self.color = "blue"
        else:
            self.color = "yellow"
        
        pygame.draw.circle(screen,self.color,self.position,self.radius,LINE_WIDTH)