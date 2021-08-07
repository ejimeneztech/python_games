import pygame, sys
from pygame import surface
from pygame.locals import *
import random
import os
import time
import settings as s


class Player(pygame.sprite.Sprite):
    def __init__(self):
       super().__init__() 
       self.image = pygame.image.load("Player.png")
       self.surf = pygame.Surface((50, 100))
       self.rect = self.surf.get_rect(center = (150, 500))
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_a]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < s.SCREEN_WIDTH:        
              if pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)