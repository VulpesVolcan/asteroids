import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS,LINE_WIDTH

class Sub_Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS + 2)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"yellow",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        movement = self.velocity *  dt
        self.position += movement