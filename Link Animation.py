##Brendan's Sprite Animation
##Chapter 13 (SPRITES)
##
##*USE ARROW KEYS TO ANIMATE*


import sys
 
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


def main():
    
    deltax=320
    deltay=240
    xspeed=0
    yspeed=0
    walkcount=0
    right=False
    left=False
    up=False
    down=False

    #main sprite sheet
    sprite_sheet=pygame.image.load("links.gif")

    #Character Idle Frame
    character=sprite_sheet.subsurface((1000,0,100,100))

    #background
    background=pygame.image.load("background.png")
    
    # Game loop.
    
    while True:
      screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

        elif event.type == pygame.KEYDOWN:
            key = event.dict['key']
            if key == pygame.K_RIGHT:
                xspeed=5
                right=True
                left=False
                up=False
                down=False
                
            if key == pygame.K_LEFT:
                xspeed=-5
                right=False
                left=True
                up=False
                down=False
                
            if key == pygame.K_UP:
                xspeed=5
                right=False
                left=False
                up=True
                down=False
            if key == pygame.K_DOWN:
                xspeed=5
                right=False
                left=False
                up=False
                down=True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                xspeed=0
                right=False
                left=False
                up=False
                down=False

                    
      
      #Background blit
      screen.blit(background,(0,0))
      
      #Walking Right  
      walk_right=sprite_sheet.subsurface((0+(walkcount%800),0,100,100))
      #Walking Left
      walk_left=sprite_sheet.subsurface((1600+(walkcount%800),0,100,100))
      #Walking Up
      walk_up=sprite_sheet.subsurface((2400+(walkcount%800),0,100,100))
      #Walking Down
      walk_down=sprite_sheet.subsurface((800+(walkcount%800),0,100,100))
      

      if right == True:
          screen.blit(walk_right,(deltax,deltay))
          walkcount+=100
          xspeed=5
          deltax=(deltax+xspeed)
          if walkcount >= 800:
              walkcount=0

      elif left == True:
          screen.blit(walk_left,(deltax,deltay))
          walkcount+=100
          xspeed=-5
          deltax=(deltax+xspeed)
          if walkcount >= 800:
              walkcount=0

      elif up == True:
          screen.blit(walk_up,(deltax,deltay))
          walkcount+=100
          yspeed=-5
          deltay=(deltay+yspeed)
          if walkcount >= 800:
              walkcount=0

      elif down == True:
          screen.blit(walk_down,(deltax,deltay))
          walkcount+=100
          yspeed=5
          deltay=(deltay+yspeed)
          if walkcount >= 800:
              walkcount=0
      else:
          screen.blit(character, (deltax,deltay))
          
      
      pygame.display.update()
      
      pygame.display.flip()
      fpsClock.tick(fps)

main()
