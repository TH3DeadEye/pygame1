import pygame
import sys
from pygame.image import load
from pygame.locals import *

pygame.init()
WIDTH, HEIGHT = 900, 450

BACKGROUND_COLOR = (97, 133, 248)  #RGB: 6185f8

pygame.display.set_caption('Super Mario Bros Remake')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#load background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(BACKGROUND_COLOR)

#load player frames
right_frames = [load('Sprite Sheet/Mario/frame1.png').convert(),
                load('Sprite Sheet/Mario/frame2.png').convert(),
                load('Sprite Sheet/Mario/frame3.png').convert()]
left_frames = [load('Sprite Sheet/Mario/frame4.png').convert(),
               load('Sprite Sheet/Mario/frame5.png').convert(),
               load('Sprite Sheet/Mario/frame6.png').convert()]

current_frames = right_frames  
current_frame = 0
frame_change_delay = 100  
last_frame_change = pygame.time.get_ticks()

#mario's initial position and movement variables
mario_x = 450
mario_y = 275
mario_speed = 5  #number of pixels Mario moves per frame
mario_rect = current_frames[current_frame].get_rect(center=(mario_x, mario_y))

right_key_pressed = False
left_key_pressed = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                right_key_pressed = True
                current_frames = right_frames  
            elif event.key == K_LEFT:
                left_key_pressed = True
                current_frames = left_frames

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                right_key_pressed = False
            elif event.key == K_LEFT:
                left_key_pressed = False

    #check : key presses
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        print('Up')
    if keys[K_DOWN]:
        print("Down")

    #animation update
    current_time = pygame.time.get_ticks()
    if right_key_pressed or left_key_pressed:
        if current_time - last_frame_change > frame_change_delay:
            current_frame = (current_frame + 1) % len(current_frames)
            last_frame_change = current_time

    #update mario's position
    if right_key_pressed:
        mario_x += mario_speed
        if mario_x > WIDTH:  #wrap mario to the left
            mario_x = -mario_rect.width
    elif left_key_pressed:
        mario_x -= mario_speed
        if mario_x < -mario_rect.width:  #wrap mario to the right
            mario_x = WIDTH

    screen.blit(background, (0, 0))
    mario_rect = current_frames[current_frame].get_rect(center=(mario_x, mario_y))
    screen.blit(current_frames[current_frame], mario_rect)

    pygame.display.flip()
    clock.tick(60) #60fps
