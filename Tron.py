#Chang Rey Tang
#Tron.py
#Game of snake with two players and each person can't bump into each other.

import pygame
import time
import random

display_width = 800
display_height = 600

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tron")
clock = pygame.time.Clock()

count1 = {"count":1}

def tron(x, y, w, h, color): 
    pygame.draw.rect(gameDisplay, color, [x,y,w,h])

def game_exit():
    pygame.quit()
    quit()

def crash():
    time.sleep(2)
    game_loop()

def game_loop():

    x1 = (display_width/2)
    y1 = (display_height*3/4)

    x1_change = 0
    y1_change = 0

    x2 = (display_width/2)
    y2 = (display_height*1/4)

    x2_change = 0
    y2_change = 0

    ex1 = 0
    ey1 = 0

    def extend1():
        pygame.draw.rect(gameDisplay, red, [ex1,ey1,10,10])
        pygame.display.update

    gameExit = False
    while not gameExit:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -10
                        y1_change = 0
                    elif event.key == pygame.K_a:
                        x2_change = -10
                        y2_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = 10
                        y1_change =0
                    elif event.key == pygame.K_d:
                        x2_change = 10
                        y2_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -10
                        x1_change = 0
                    elif event.key == pygame.K_w:
                        y2_change = -10
                        x2_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = 10
                        x1_change = 0
                    elif event.key == pygame.K_s:
                        y2_change = 10
                        x2_change = 0

            ex1 = x1
            x1 += x1_change
            x2 += x2_change
            ey1 = y1
            y1 += y1_change
            y2 += y2_change

            gameDisplay.fill(white)

            tron(x1,y1,10,10,red) #def tron(x, y, w, h, color)
            tron(x2,y2,10,10,blue)

            extend1()
            extend1()
            extend1()

            if x1 > (display_width-10) or x1 < 0 or x2 > (display_width-10) or x2 < 0:
                crash() #run crash function

            if y1 < 0 or y1 > (display_height-10) or y2 < 0 or y2 > (display_height-10):
                crash()

            pygame.display.update()
            clock.tick(30)

game_loop()
game_exit()


            
                        
