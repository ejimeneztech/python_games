#https://coderslegacy.com/python/python-pygame-tutorial/
#Add Health bar (using 2 rects [green and redS]). When health bar goes down to 0 reduce 1 life from player. When LIVES = 0, game over.


import pygame, sys
from pygame import surface
from pygame.locals import *
import random
import os
import time

 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
LIVES = 3
#create health variable
HEALTH = 200

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Speed Chase")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((50, 80))
        self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-40)
                                               ,0))     
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

      
      def self_destruct(self):
          self.kill()
          
   
 
 
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
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_d]:
                  self.rect.move_ip(5, 0)
 


       

#setting up sprites         
P1 = Player()
E1 = Enemy()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


while True:     
    for event in pygame.event.get():              
        if event.type == INC_SPEED:
              SPEED += 2
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
     
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    lives_remaining = font_small.render(str(LIVES),True, BLACK)
    DISPLAYSURF.blit(lives_remaining, (10, 40))

  
    #draw health bar
    
    pygame.draw.rect(DISPLAYSURF, RED, (10, 65, 200, 5))
    pygame.draw.rect(DISPLAYSURF, GREEN, (10, 65, HEALTH, 5))

    
        #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    
    #To be run if collision occurs between Player and Enemy
    for enemy in enemies:
        if pygame.sprite.spritecollideany(P1, enemies):
            HEALTH -= 50
            #enemy.self_destruct(); removed this because it ends the game since there is only 1 enemy sprite being moved around the screen
            enemy.rect = enemy.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-40)
                                               ,0))
            
            
            if HEALTH  == 0 and LIVES > 0:
               HEALTH += 200
               LIVES -= 1
            
            
            if LIVES == 0:
           
                DISPLAYSURF.fill(RED)
                DISPLAYSURF.blit(game_over, (30,250))

                pygame.display.update()
                for entity in all_sprites:
                        entity.kill() 
                time.sleep(2)
                pygame.quit()
                sys.exit()      

    
    

    pygame.display.update()
    FramePerSec.tick(FPS)
