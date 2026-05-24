import pygame
from constants import *
from player import Player
from shot import Shot
color = "white"




class Drone(Player):
   def __init__(self,x,y,parent):
      super().__init__(x,y)
      self.parent = parent
      self.offset = 5

   def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius // 3
        b = self.position - forward * self.radius - right // 3
        c = self.position - forward * self.radius + right // 3
        return [a, b, c] 
    
   def draw(self,screen):
      pygame.draw.polygon(screen,color,self.triangle(),LINE_WIDTH)
        
   def update(self, dt):
        self.cooldown -= dt
        self.sub_cooldown -= dt
        self.boost_cooldown -= dt
        keys = pygame.key.get_pressed()
        self.rotation = self.parent.rotation
        
        if keys[pygame.K_w]:
            self.move(dt)
       
        if keys[pygame.K_s]:
            self.move(-dt)
   
        if keys[pygame.K_SPACE]:
            self.shoot()

    
   def move(self,dt):
      Player.move(self,dt)
   
   def shoot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        bullet = Shot(self.position[0],self.position[1],SHOT_RADIUS)
        bullet_vector = pygame.Vector2(0, 1)
        rotated_bullet_vector = bullet_vector.rotate(self.rotation)
        bullet.velocity = rotated_bullet_vector * PLAYER_SHOOT_SPEED 
           