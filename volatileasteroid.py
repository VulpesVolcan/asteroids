import pygame,random
from asteroid import Asteroid
from constants import LINE_WIDTH as width
from logger import log_event
from asteroid import Asteroid

class Volatile_Asteroid(Asteroid):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius,"V")
        print(f"Volatile_Asteroid radius: {self.radius}")
        self.color = "red"
        self.center_color = "yellow"
        self.iframes = 0
        self.times_hit = 0

    def draw(self,screen):
        shell = pygame.draw.circle(screen,self.color,self.position,self.radius,width)
        core = pygame.draw.circle(screen,self.center_color,self.position,self.radius // 1.5,width)
        shell 
        core

    def update(self,dt):
        movement = self.velocity * dt
        self.position += movement
        

    def split(self):
        self.kill()


    def detonate(self):
        if self.radius == 5:
            self.kill()
        self.times_hit += 1
        if self.times_hit < 3:
            return
        self.kill()
        log_event("asteroid_detonate")
        new_angle = random.uniform(0,360)
        vel1 = self.velocity.rotate(new_angle)
        vel2 = self.velocity.rotate(-new_angle)
        vel3 = self.velocity.rotate(new_angle / 2)
        vel4 = self.velocity.rotate(-new_angle // 2)
        new_radius = 5

        first_shard = Asteroid(self.position[0],self.position[1],new_radius,"N")
        first_shard.velocity = vel1

        second_shard = Asteroid(self.position[0],self.position[1],new_radius,"N")
        second_shard.velocity = vel2

        third_shard = Asteroid(self.position[0],self.position[1],new_radius,"N")
        third_shard.velocity = vel3

        fourth_shard = Asteroid(self.position[0],self.position[1],new_radius,"N")
        fourth_shard.velocity = vel4