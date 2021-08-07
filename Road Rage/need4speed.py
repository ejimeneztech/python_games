import pygame, sys
from pygame import surface
from pygame.locals import *
import random
import os
import time
import enemy as e
import player as p
import settings as s
import start_screen as ss
#https://coderslegacy.com/python/python-pygame-tutorial/
#Display start screen; wait for user input
ss.menu_screen()

pygame.init()
 


#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, s.BLACK)

background = pygame.image.load("AnimatedStreet.png")
 
DISPLAYSURF = pygame.display.set_mode((s.SCREEN_WIDTH,s.SCREEN_HEIGHT))
DISPLAYSURF.fill(s.WHITE)
pygame.display.set_caption("Road Rage")
 

#setting up sprites         
P1 = p.Player()
E1 = e.Enemy()


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
              s.SPEED += 2
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
     
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(s.SCORE), True, s.BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    lives_remaining = font_small.render(str(s.LIVES),True, s.BLACK)
    DISPLAYSURF.blit(lives_remaining, (10, 40))

  
    #draw health bar
    
    pygame.draw.rect(DISPLAYSURF, s.RED, (10, 65, 200, 5))
    pygame.draw.rect(DISPLAYSURF, s.GREEN, (10, 65, s.HEALTH, 5))

    
        #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    
    #To be run if collision occurs between Player and Enemy
    for enemy in enemies:
        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            s.HEALTH -= 50
            #enemy.self_destruct(); removed this because it ends the game since there is only 1 enemy sprite being moved around the screen
            enemy.rect = enemy.surf.get_rect(center = (random.randint(40, s.SCREEN_WIDTH-40)
                                               ,0))
            
            
            if s.HEALTH  == 0 and s.LIVES > 0:
               s.HEALTH += 200
               s.LIVES -= 1
            
            
            if s.LIVES == 0:
           
                DISPLAYSURF.fill(s.RED)
                DISPLAYSURF.blit(game_over, (30,250))

                pygame.display.update()
                for entity in all_sprites:
                        entity.kill() 
                time.sleep(2)
                pygame.quit()
                sys.exit()      

    
    

    pygame.display.update()
    s.FramePerSec.tick(s.FPS)
