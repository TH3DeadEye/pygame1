import pygame 
from pygame.image import load
BASE_IMG_PATH = 'Sprite Sheet/'

def load_images(path):
    img = load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((107,49,156))

    return img

#C:\Users\Arman\Desktop\new-folder\Folders\programs\python\pygame\pygame1\Sprite Sheet\Tiles