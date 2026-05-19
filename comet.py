import pygame,random
from asteroid import Asteroid
from constants import LINE_WIDTH as width
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Comet(Asteroid):
    def __init__(self, x, y, radius,ID):
        super().__init__(x, y, radius)
        self.color = "white"
        self.flash_timer = 0
        self.iframes = 0
        self.ID = ID
        if self.ID == "V":
            self.color = "red"

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius,width)

    def update(self,dt):
        movement = self.velocity * dt
        self.position += movement
        if self.radius == 5:
            self.color = "red"
            return
        self.find_color(dt)

    def split(self):
        self.kill()
        