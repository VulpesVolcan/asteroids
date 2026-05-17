import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot
from piercingshot import Piercing_Shot
color = "white"

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.sub_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] 
    
    def draw(self,screen):
        pygame.draw.polygon(screen,color,self.triangle(),LINE_WIDTH)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        self.cooldown -= dt
        self.sub_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
           self.rotate(-dt)

        if keys[pygame.K_d]:
           self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)
       
        if keys[pygame.K_s]:
            self.move(-dt)
   
        if keys[pygame.K_SPACE]:
            self.shoot()

        if keys[pygame.K_m]:
            self.piercing()

    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        bullet = Shot(self.position[0],self.position[1],SHOT_RADIUS)
        bullet_vector = pygame.Vector2(0, 1)
        rotated_bullet_vector = bullet_vector.rotate(self.rotation)
        bullet.velocity = rotated_bullet_vector * PLAYER_SHOOT_SPEED 
           
    def piercing(self):
        if self.sub_cooldown > 0:
            return
        self.sub_cooldown = PLAYER_SPECIAL_SHOOT_COOLDOWN_SECONDS
        bullet = Piercing_Shot(self.position[0],self.position[1],SHOT_RADIUS)
        bullet_vector = pygame.Vector2(0, 1)
        rotated_bullet_vector = bullet_vector.rotate(self.rotation)
        bullet.velocity = rotated_bullet_vector * PLAYER_PIERCING_SHOOT_SPEED 
