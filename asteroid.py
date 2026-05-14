import pygame,random
from circleshape import CircleShape
from constants import LINE_WIDTH as width
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width)

    def update(self,dt):
        movement = self.velocity * dt
        self.position += movement

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        split_1 = self.velocity.rotate(new_angle)
        split_2 = self.velocity.rotate(-new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position[0],self.position[1],new_radius)
        first_asteroid.velocity = split_1
    
        second_asteroid = Asteroid(self.position[0],self.position[1],new_radius)
        second_asteroid.velocity = split_2
        return first_asteroid,second_asteroid