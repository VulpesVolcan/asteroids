import pygame,random
from circleshape import CircleShape
from constants import LINE_WIDTH as width
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius,ID):
        super().__init__(x, y, radius)
        self.color = "white"
        self.flash_timer = 0
        self.iframes = 0
        self.ID = ID
        if self.ID == "V":
            self.color = "red"
   
    def find_color(self,dt):
        self.flash_timer += dt
        colors = ["red","blue","green"]
        random.shuffle(colors)
        if self.flash_timer >= 0.25:
         self.flash_timer = 0
         self.color = colors[0]
      

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,self.position,self.radius,width)

    def update(self,dt):
        movement = self.velocity * dt
        self.position += movement
        if self.ID != "N":
            self.color = "red"
            movement = self.velocity * (dt * 2)
            self.position += movement
            
            
            
            return
        self.find_color(dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        split_1 = self.velocity.rotate(new_angle)
        split_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0],self.position[1],new_radius,"N")
        first_asteroid.velocity = split_1
    
        second_asteroid = Asteroid(self.position[0],self.position[1],new_radius,"N")
        second_asteroid.velocity = split_2
        return first_asteroid,second_asteroid