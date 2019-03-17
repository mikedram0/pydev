import sys
import pygame
import time
import math
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ship = pygame.image.load("starship.png")
shiprect = ship.get_rect()
x=width/2
y=height/2
vx=0
vy=0
angle=0
anglev=0
FPS=60

while 1:
    time.sleep(1/FPS)
    angle=angle+anglev
    #print(1)
    for event in pygame.event.get():
        #print(2)
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            

            if event.key==pygame.K_a:
                anglev=anglev+1
                

            if event.key==pygame.K_d:
                anglev=anglev-1


            if event.key == pygame.K_w:
                vx += math.sin(angle*3.1415/180 +3.1415) 
                vy += math.cos(angle*3.1415/180+3.1415) 


    x += vx
    y += vy

    if x-shiprect[2]>width:
        x = 0 - shiprect[1]
    if x+shiprect[2]<0:
        x = width
    if y>height:
        y = 0 - shiprect[3]
    if y<0-shiprect[3]:
        y = height
        

    old=shiprect.center
    new_ship=pygame.transform.rotate(ship,angle)
    shiprect = new_ship.get_rect()
    shiprect.center=old

    screen.fill(black)
    screen.blit(new_ship, (x,y))
    pygame.display.update()

pygame.quit()
quit()

