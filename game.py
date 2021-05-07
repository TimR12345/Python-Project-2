#Made with inspiration from pygame
#I know it would be better with collision, however I cant get it to work and really dont understand it yet.
#Timothy Rohe
#3/30/21

import pygame, sys
from pygame.locals import *
import random
#initialize game
pygame.init()
#giving a value to FPS
FPS = 60
FramePerSec = pygame.time.Clock()
#Determining Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#Setting up display
DISPLAYSURF = pygame.display.set_mode((400,500))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Slider game")
#defining the sprite for the enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, 360)
                                               ,0))     
 		
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(pygame.Surface((50,80)), self.rect) 
 
#defining the sprite for the player sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center = (150, 500))
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < (400):        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(pygame.Surface((50,80)), self.rect)     
 
         
player1 = Player()
enemy1 = Enemy()
#game loop
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    player1.update()
    enemy1.move()
     
    DISPLAYSURF.fill(WHITE)
    player1.draw(DISPLAYSURF)
    enemy1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)