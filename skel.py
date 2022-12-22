# skeleton code for project 2
# vis 142 fall 2022 
# This can take 20 minutes to hours to run.

import pygame
from pygame.locals import *
from sys import exit
import random
import time
import animation

start_time = time.time()

width = 1920 
height = 1080 
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill((0,0,0))
frame_num = 0

# this function makes one second of black frames
def make_black():
    global frame_num
    screen.fill((0,0,0))
    pygame.display.update()
    for i in range(0, 60):
    #    pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
       frame_num = frame_num + 1
       clock.tick(60)
        
frames = [pygame.image.load("1.png"), pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png")]
frameTime = [8,6,9,11]
repeat = True

frames = [pygame.image.load("1.png"), pygame.image.load("2.png"), pygame.image.load("3.png"), pygame.image.load("4.png")]
frameTime = [2,2,2,2]
repeat = True

anim = animation.animation(frames, frameTime, repeat)
x = 200
# here is the main animation loop
for i in range(0, 20*60): # 20*60 frames is 20 seconds
    #########################################################
    # in the skeleton, your animation goes from here ########
    #########################################################
    
    anim.update(screen, pygame.Rect(x,200,10,10))
    x = x + 1
    #########################################################
    # to here ###############################################
    #########################################################
    # print out stats
   
    # The next line can be commented out to speed up testing frame rate
    # by not writing the file. But for output to final frames,
    # you will need to ucomment it.
    # pygame.image.save(screen, "./frames/" + str(frame_num) + ".png")
    frame_num = frame_num + 1
    pygame.display.update()
    clock.tick(60)

# print out stats
print("seconds:", int(time.time() - start_time))
print("~minutes: ", int((time.time() - start_time)/60))
print(frame_num)
# we just quit here
pygame.display.quit()
pygame.quit()
exit()

# you can make your files into a movie with ffmpeg:
# ffmpeg -r 60 -start_number 1000000 -s 4096x2160 -i %d.png -vcodec libx264 -crf 5 -pix_fmt yuv420p final.mp4
# with a few changes such as to start number, but this is just extra info here
