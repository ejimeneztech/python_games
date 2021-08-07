import pygame, sys
from pygame import surface
from pygame.locals import *
import random
import os
import time
import settings as s

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, s.SCREEN_WIDTH-40)
                                               ,0))     
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,s.SPEED)
        if (self.rect.bottom > 600):
            s.SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

      
      def self_destruct(self):
          self.kill()