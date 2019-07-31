#??/Demo
#IMPORTS===============================================================================================================================================================================================================================================================================================================================================================================
import sys
import os
import pygame
import time
import random
from pygame.locals import*

#WINDOW========================================================================================================================================================================================================================================================================================================================================================================================
windowHeight = 800
windowWidth = 1600
surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)
pygame.display.set_caption("??")

#IMAGES==================================================================================================================================================================================================================================================================================================================================================================================================
#Player
playerImage = pygame.image.load("player.png")

#Effects
frozenImage = pygame.image.load('frozen.png')
#Floor
floorImage = pygame.image.load('floor.png')
dangerfloorImage = pygame.image.load('danger_floor.png')
freezefloorImage = pygame.image.load('freeze_floor.png')
shockImage = pygame.image.load('electiction.png')
electricfloorImage = pygame.image.load('electric_floor.png')
#DICT.=======================================================================================================================================================================================================================================================================================================================================================================================================================================
#Player
player = {
    'rect' : playerImage.get_rect(),
    'feet' : playerImage.get_rect(),
    'faceing_right' : True,
    'faceing_left' : False
    }
player['rect'].x = 400
player['rect'].y = 0
player['feet'].x = 400
player['feet'].y = 45
player['feet'].height = 15 
player['feet'].width = 60
#Floor
floor = {}

#LISTS============================================================================================================================================================================================================================================================================================================================================================================================================
#Levels
#Bottom Layer
level_one = []
floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 190
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 330
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 470
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 610
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 750
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 890
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1, 
         'count' : 800
         }
floor['rect'].x = 1030
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 1170
floor['rect'].y = 600
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 1310
floor['rect'].y = 600
level_one.append(floor)

#Middle Layer
##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 190
##floor['rect'].y = 395
##level_one.append(floor)
##
##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 330
##floor['rect'].y = 395
##level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 470
floor['rect'].y = 395
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 610
floor['rect'].y = 395
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 750
floor['rect'].y = 395
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 890
floor['rect'].y = 395
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 1030
floor['rect'].y = 395
level_one.append(floor)

##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 1170
##floor['rect'].y = 395
##level_one.append(floor)
##
##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 1310
##floor['rect'].y = 395
##level_one.append(floor)
#Top Layer

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 190
floor['rect'].y = 190
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 330
floor['rect'].y = 190
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1, 
         'count' : 800
         }
floor['rect'].x = 470
floor['rect'].y = 190
level_one.append(floor)

##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 610
##floor['rect'].y = 190
##level_one.append(floor)

##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 750
##floor['rect'].y = 190
##level_one.append(floor)
##
##floor = {'rect': floorImage.get_rect(),
##         'image' : floorImage,
##         'visible' : True,
##         'type' : 1,
##         'count' : 800
##         }
##floor['rect'].x = 890
##floor['rect'].y = 190
##level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 1030
floor['rect'].y = 190
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 1170
floor['rect'].y = 190
level_one.append(floor)

floor = {'rect': floorImage.get_rect(),
         'image' : floorImage,
         'visible' : True,
         'type' : 1,
         'count' : 800
         }
floor['rect'].x = 1310
floor['rect'].y = 190
level_one.append(floor)
#VARIABLES==================================================================================================================================================================================================================================================================================================================================================================================================
#Floor
shock = False
shock_count = 0
freeze = False
freeze_count = 0
pause = 0
bad = 0
#Buttons
left = False
right = False
up = False
down = False
active = False
count = 0
#Colors
BLACK = (0,0,0)
#FPS
clock = pygame.time.Clock()
#FUNCTIONS===========================================================================================================================================================================================================================================================================================================================================================================================
def touching_ground():
    global freeze, shock
    for f in level_one:
        if player['feet'].colliderect(f['rect']) and f['visible'] == True:
            if (player['feet'].y > f['rect'].y) and (player['feet'].y < f['rect'].y +35):
                player['feet'].y = f['rect'].y - 23
                player['rect'].y = f['rect'].y - 68
            if f['type'] == 2 and freeze == False:
                freeze = True
            elif f['type'] == 3:
                shock = True
            return True
       


def gravity():
    global player
    if not touching_ground() and active == False:
        player['rect'].y += 3
        player['feet'].y += 3
        
        
        
#Player
def player_movement():
    global player, up, count, active, down, freeze
    if left == True and freeze == False:
        player['rect'].x -= 3
        player['feet'].x -= 3
    elif right == True and freeze == False:
        player['rect'].x += 3
        player['feet'].x += 3
    if up == True and freeze == False:
        player['rect'].y -= 5
        player['feet'].y -= 5
        count += 1
        if count == 55:
            up = False
            active = False
            count = 0
    elif down == True and freeze == False:
        player['rect'].y += 50
        player['feet'].y += 50
        down = False
        
        
            


def draw_player():
    surface.blit(playerImage,(player['rect'].x, player['rect'].y))
    if freeze == True:
        surface.blit(frozenImage,(player['rect'].x, player['rect'].y))
    elif shock == True:
        surface.blit(shockImage,(player['rect'].x, player['rect'].y))  
#Floor
def draw_floor():
    for f in level_one:
        if f['count'] < 800:
            f['count'] -= .25
            if f['type'] == 2:
                f['image'] = freezefloorImage
            elif f['type'] == 3:
                f['image'] = electricfloorImage 
            else:
                f['image'] = dangerfloorImage
        if f['count'] <= 400:
            if f['type'] == 2 or f['type'] == 3:
                f['count'] = 800
                f['image'] = floorImage
                f['type'] = 1
            else:
                f['visible'] = False
                
        if f['count'] <= 0:
            f['visible'] = True
            f['count'] = 800
            f['image'] = floorImage
        if f['visible'] == True:
            surface.blit(f['image'],(f['rect'].x,f['rect'].y))
        
def choosing_floor():
    
    global bad, level_one, freeze
    bad = random.choice(level_one)
    if bad['count'] == 800:
        bad['count'] = 799
    x = random.randint(1,6)
    if x == 2:
        bad['type'] = 2
    elif x == 5:
        bad['type'] = 3
    
#GAME LOOP=======================================================================================================================================================================================================================================================================================================================================================================================================
while True:
    for event in pygame.event.get():
        mousex,mousey = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
              
            elif event.key == pygame.K_RIGHT:
                right = True
                
            if event.key == pygame.K_UP:
                up = True
                active = True
            elif event.key == pygame.K_DOWN:
                down = True 

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            elif event.key == pygame.K_RIGHT:
                right = False
               
    surface.fill(BLACK)
    if pause == 800:
        choosing_floor()
        pause = 0
    pause += 1
    if freeze == True:
        freeze_count += 1
    if freeze_count == 120:
        freeze = False
        freeze_count = 0
    if shock == True:
        shock_count += 1
    if shock_count == 120:
        shock = False
        shock_count = 0
    gravity()
    player_movement()
    draw_floor()
    draw_player()
    pygame.display.update()
  
                
            
        
        
        
    
