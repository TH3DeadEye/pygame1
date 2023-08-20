import pygame ,sys
from pygame.image import load

pygame.init()
WIDGHT, HEIGHT = 900 , 450

pygame.display.set_caption('Super Mario Bros Remake')
screen = pygame.display.set_mode((WIDGHT, HEIGHT))
clock = pygame.time.Clock()

#loading player
marrio_surface = load('Sprite Sheet/Mario/Untitled-1.png').convert()
marrio_rect = marrio_surface.get_rect(center = (450 , 275))



#game loop
while True:
    #quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('Up')
            if event.key == pygame.K_DOWN:
                print("down")
            if event.key == pygame.K_RIGHT:
                print('right')
            if event.key == pygame.K_LEFT:
                print("left")
    screen.blit(marrio_surface, marrio_rect)






    pygame.display.update()
    clock.tick(60)

    #print(int(clock.get_fps()))