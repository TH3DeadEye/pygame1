import pygame ,sys
from pygame.image import load

pygame.init()
WIDGHT, HEIGHT = 900 , 450

pygame.display.set_caption('First Game')
screen = pygame.display.set_mode((WIDGHT, HEIGHT))
clock = pygame.time.Clock()

test = load('Vision.png')
#game loop
while True:
    #quiting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)

    screen.blit(test, (0,0))

    print(int(clock.get_fps()))