import pygame
import sys
from pygame.image import load
from pygame.locals import *

#constants
WIDTH, HEIGHT = 900, 450
BACKGROUND_COLOR = (97, 133, 248)  #RGB: 6185f8
FRAME_DELAY = 100  #milliseconds
GRAVITY = 5  #acceleration due to gravity
JUMP_STRENGTH = -20  #strength of the jump

#initialize Pygame
pygame.init()
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
last_frame_change = pygame.time.get_ticks()

#mario's initial position and movement variables
mario_x = 100
mario_y = 250
mario_speed = 5
mario_rect = current_frames[current_frame].get_rect(topleft=(mario_x, mario_y))

right_key_pressed = False
left_key_pressed = False
is_jumping = False
jump_count = 0

#load goomba frames
goomba_frames = [load('Sprite Sheet/Goomba/frame1.png').convert(),
                 load('Sprite Sheet/Goomba/frame2.png').convert()]

current_goomba_frame = 0
last_goomba_frame_change = pygame.time.get_ticks()

goomba_speed = 2  #goomba's movement speed
goomba_x = 700  #initial Goomba position
goomba_y = 385
goomba_rect = goomba_frames[current_goomba_frame].get_rect(topleft=(goomba_x, goomba_y))
goomba_direction = -1  #goomba moves to the left initially

#define the ground platform (x,y,width,height)
ground = (0, 400, WIDTH, 20)

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
            elif event.key == K_UP and not is_jumping:
                is_jumping = True
                jump_count = 20  #adjust the jump height by changing this value

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                right_key_pressed = False
            elif event.key == K_LEFT:
                left_key_pressed = False

    #animation update for mario
    current_time = pygame.time.get_ticks()
    if right_key_pressed or left_key_pressed:
        if current_time - last_frame_change > FRAME_DELAY:
            current_frame = (current_frame + 1) % len(current_frames)
            last_frame_change = current_time

    #animation update for goomba
    if current_time - last_goomba_frame_change > FRAME_DELAY:
        current_goomba_frame = (current_goomba_frame + 1) % len(goomba_frames)
        last_goomba_frame_change = current_time

    #update mario's position and apply gravity
    if right_key_pressed:
        mario_x += mario_speed
    elif left_key_pressed:
        mario_x -= mario_speed

    if is_jumping:
        mario_y -= jump_count
        jump_count -= 1
        if jump_count < 0:
            is_jumping = False

    mario_y += GRAVITY  #apply gravity

    #collision detection with the ground
    mario_rect.topleft = (mario_x, mario_y)
    if mario_rect.colliderect(ground) and not is_jumping:
        mario_y = ground[1] - mario_rect.height
        jump_count = 0

    #update goomba's position
    goomba_x += goomba_speed * goomba_direction

    #reverse goomba's direction if it reaches the screen edges
    if goomba_x < 0:
        goomba_direction = 1  #move to the right
    elif goomba_x + goomba_rect.width > WIDTH:
        goomba_direction = -1  #move to the left

    #check for collision between Mario and Goomba
    if mario_rect.colliderect(goomba_rect):
        print("mario touched goomba")
    
    screen.blit(background, (0, 0))
    mario_rect.topleft = (mario_x, mario_y)
    goomba_rect.topleft = (goomba_x, goomba_y)

    #draw the ground
    pygame.draw.rect(screen, (255, 0, 0), ground)

    screen.blit(current_frames[current_frame], mario_rect)
    screen.blit(goomba_frames[current_goomba_frame], goomba_rect)

    pygame.display.flip()
    clock.tick(60)  #60FPS
