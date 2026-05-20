import pygame,random
from asteroid import Asteroid
from constants import LINE_WIDTH as width
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Comet(Asteroid):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius,"C")
        self.color = "orange"
        self.flash_timer = 0
        self.iframes = 0
        
        

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius,width)
        particle = pygame.draw.circle(screen,"yellow",self.position,2,width)
        particle

    def update(self,dt):
        movement = self.velocity * (dt * 5)
        self.position += movement
        
    
    def split(self):
        self.kill()
        